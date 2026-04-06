from memory import read_memory, write_memory, fill_program_memory, memory_to_str
from error import SimulatorError
from register import read_register, write_register, registers_to_str, register_extract
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

try:
    with open(input_machine_code_path, 'r') as f:
        lines = f.readlines()
        fill_program_memory(lines)
    
    with open(output_trace_path, 'w') as f:
        while True:

            # Fetch
            pc = getPC()
            instruction = read_memory(pc, 4)
            if instruction == halt_instruction:
                break
            
            PCPlus4 = pc + 4


            # Decode
            decode_instruction(instruction)
            controls = get_controls()

            immediate = ImmExt(instruction, controls["ImmSrc"])

            register_file = register_extract(instruction)


            # execute
            PCTarget = pc + immediate

            SrcA = read_register(register_file["rd1"])
            SrcB = immediate if controls["ALUSrc"] else read_register(register_file["rd2"])
            ALUResult = ALU(SrcA, SrcB, controls["ALUControl"])

            Zero = ALUResult == 0

            WriteData = read_register(register_file["rd2"])


            # memory
            if controls["MemWrite"]:
                write_memory(address=ALUResult, bytes=4, value=WriteData)

            Result = ALUResult if controls["ResultSrc"] == 0 else read_memory(address=ALUResult, bytes=4)


            # write back
            if controls["RegWrite"]:
                write_register(reg=register_file["wd3"], value=Result)

            if controls["PCSrc"]:
                PCNext = PCTarget
            elif controls["ImmSrc"] == 2:   # B-type instruction
                PCNext = PCTarget if Zero else PCPlus4
            else:
                PCNext = PCPlus4
            PCjump(newPC=PCNext)




            f.write(f"0b{pc:032b}" + registers_to_str() + "\n")
        
        f.write(memory_to_str())

except SimulatorError as e:
    print(e)