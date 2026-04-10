from memory import read_memory, write_memory, fill_program_memory, memory_to_str, memory_to_str_readable
from error import SimulatorError
from register import read_register, write_register, registers_to_str, register_extract, registers_to_str_readable
from program_counter import getPC, PCjump
from control_unit import get_controls, decode_instruction
import sys
from extend import ImmExt
from ALU import ALU

try:
    input_machine_code_path = sys.argv[1]
except IndexError:
    print("input_machine_code_path not given")
    sys.exit(1)

try:
    output_trace_path = sys.argv[2]
except IndexError:
    print("output_trace_path not given")
    sys.exit(1)

try:
    output_readable_path = sys.argv[3]
except IndexError:
    output_readable_path = ""


halt_instruction = 0

readable = ""

try:
    with open(input_machine_code_path, 'r') as f:
        lines = f.readlines()
        fill_program_memory(lines)
    
    with open(output_trace_path, 'w') as f:
        while True:
            # Fetch
            pc = getPC()
            instruction = read_memory(pc, 4)
            if opcode == 0x63 and funct3 == 0x0:
                rs1 = (instruction >> 15) & 0x1F
                rs2 = (instruction >> 20) & 0x1F
                imm = immediate

                if rs1 == 0 and rs2 == 0 and imm == 0:
                    break
            
            PCPlus4 = pc + 4
            opcode = instruction & 0x7F
            funct3 = (instruction >> 12) & 0x7

            # Decode
            decode_instruction(instruction)
            controls = get_controls()
            immediate = ImmExt(instruction, controls["ImmSrc"])
            register_file = register_extract(instruction)

            # --- EXECUTE ---
            # Fix 1: SrcA for AUIPC must be the PC, not a register
            if opcode == 0x17:
                SrcA = pc
            else:
                SrcA = read_register(register_file["rd1"])

            SrcB = immediate if controls["ALUSrc"] else read_register(register_file["rd2"])
            ALUResult = ALU(SrcA, SrcB, controls["ALUControl"])
            
            Zero = (ALUResult == 0)
            WriteData = read_register(register_file["rd2"])

            # --- MEMORY ---
            if controls["MemWrite"]:
                write_memory(address=ALUResult, bytes=4, value=WriteData)

            # --- RESULT SELECTION ---
            # Fix 2: Order matters. LUI/AUIPC use the immediate/ALU result directly.
            if opcode == 0x37:     # LUI
                Result = immediate
            elif opcode == 0x17:
                Result = (pc + immediate) & 0xFFFFFFFF
            elif controls["ResultSrc"] == 1: # Load instructions
                Result = read_memory(address=ALUResult, bytes=4)
            else:                  # Standard R/I type
                Result = ALUResult

            # --- WRITE BACK ---
            if controls["RegWrite"]:
                write_register(reg=register_file["wd3"], value=Result)

            # --- NEXT PC SELECTION ---
            PCTarget = pc + immediate
            
            if controls["PCSrc"]: 
                # JAL uses PCTarget (pc + imm), JALR uses ALUResult (rs1 + imm)
                if opcode == 0x6F: # JAL
                    PCNext = PCTarget
                else:              # JALR (opcode 0x67)
                    PCNext = ALUResult & ~1 # RISC-V spec: force LSB to 0
            elif controls["ImmSrc"] == 2: # B-types
                take_branch = False
                if funct3 == 0x0:   take_branch = Zero       # beq
                elif funct3 == 0x1: take_branch = not Zero   # bne
                elif funct3 == 0x4: take_branch = (ALUResult == 1) # blt (if ALU returns 1)
                elif funct3 == 0x5: take_branch = (ALUResult == 0) # bge (if SLT returns 0)
                elif funct3 == 0x6: take_branch = (ALUResult == 1) # bltu
                elif funct3 == 0x7: take_branch = (ALUResult == 0) # bgeu
                
                PCNext = PCTarget if take_branch else PCPlus4
            else:
                PCNext = PCPlus4

            PCjump(newPC=PCNext)
        
        f.write(memory_to_str())
        readable += memory_to_str_readable()

except SimulatorError as e:
    line = (pc // 4) + 1
    print(f"Error at line {line}: {e}")

finally:
    if output_readable_path:
        with open(output_readable_path, 'w') as f:
            f.write(readable)