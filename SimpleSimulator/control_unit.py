from error import SimulatorError

opcode = 0
funct3 = 0
funct7 = 0

PCsrc = 0
ResultSrc = 0
MemWrite = 0
ALUControl = 0
ALUSrc = 0
ImmSrc = 0
RegWrite = 0

def decode_instruction(instruction: int):
    global opcode, funct3, funct7
    global PCsrc, ResultSrc, MemWrite, ALUControl, ALUSrc, ImmSrc, RegWrite
    opcode = instruction & 0x7F
    funct3 = (instruction >> 12) & 0x7
    funct7 = (instruction >> 25) & 0x7F

    PCsrc = 0
    ResultSrc = 0
    MemWrite = 0
    ALUControl = 0
    ALUSrc = 0
    ImmSrc = 0
    RegWrite = 0

    if opcode == 0x33:
        RegWrite = 1
        ALUSrc = 0
        MemWrite = 0
        ResultSrc = 0

        if funct3 == 0x0:
            if funct7 == 0x00:
                ALUControl = 0b0010   # ADD
            elif funct7 == 0x20:
                ALUControl = 0b0110   # SUB

        elif funct3 == 0x1:
            ALUControl = 0b0011   # SLL

        elif funct3 == 0x2:
            ALUControl = 0b0100   # SLT

        elif funct3 == 0x3:
            ALUControl = 0b0101   # SLTU

        elif funct3 == 0x4:
            ALUControl = 0b0111   # XOR

        elif funct3 == 0x5:
            ALUControl = 0b1000   # SRL

        elif funct3 == 0x6:
            ALUControl = 0b0001   # OR

        elif funct3 == 0x7:
            ALUControl = 0b0000   # AND

    elif opcode == 0x13:
        RegWrite = 1
        ALUSrc = 1
        MemWrite = 0
        ResultSrc = 0
        ImmSrc = 0

        ALUControl = 0b0010   # ADD

    elif opcode == 0x03:
        RegWrite = 1
        ALUSrc = 1
        MemWrite = 0
        ResultSrc = 1
        ImmSrc = 0

        ALUControl = 0b0010   # ADD

    elif opcode == 0x23:
        RegWrite = 0
        ALUSrc = 1
        MemWrite = 1
        ImmSrc = 1
        ResultSrc = 0

        ALUControl = 0b0010   # ADD

    elif opcode == 0x63:  # B-type instructions
        RegWrite = 0
        ALUSrc = 0        # Branches compare two registers (rs1, rs2)
        MemWrite = 0
        ImmSrc = 2        # B-type immediate decoding
        ResultSrc = 0     # Not writing to registers, so ResultSrc is technically 'don't care'

        # Map funct3 to ALUControl operations
        if funct3 == 0x0:      # beq: check if rs1 - rs2 == 0
            ALUControl = 0b0110 # SUB
        elif funct3 == 0x1:    # bne: check if rs1 - rs2 != 0
            ALUControl = 0b0110 # SUB (Logic handled by PCSrc logic outside decode)
        elif funct3 == 0x4:    # blt: rs1 < rs2 (signed)
            ALUControl = 0b0100 # SLT (Set Less Than)
        elif funct3 == 0x5:    # bge: rs1 >= rs2 (signed)
            ALUControl = 0b0100 # SLT (If SLT returns 0, then rs1 >= rs2)
        elif funct3 == 0x6:    # bltu: rs1 < rs2 (unsigned)
            ALUControl = 0b0101 # SLTU (Set Less Than Unsigned)
        elif funct3 == 0x7:    # bgeu: rs1 >= rs2 (unsigned)
            ALUControl = 0b0101 # SLTU
        else:
            raise SimulatorError(f"Unsupported B-type funct3: {hex(funct3)}")

    elif opcode == 0x6F:
        RegWrite = 1
        ALUSrc = 0
        MemWrite = 0
        ImmSrc = 3
        PCsrc = 1

        ALUControl = 0b0010   # ADD

    elif opcode == 0x67:
        RegWrite = 1
        ALUSrc = 1
        MemWrite = 0
        ImmSrc = 0
        PCsrc = 1

        ALUControl = 0b0010   # ADD

    elif opcode == 0x37:
        RegWrite = 1
        ALUSrc = 1      # Use immediate
        MemWrite = 0
        ImmSrc = 4      # New ImmSrc type for U-type (20-bit)
        ResultSrc = 0   # Take the result from the ALU/Path
        ALUControl = 0b1010 # New ALU operation: LUI_COPY (just pass Imm through)

    elif opcode == 0x17:
        RegWrite = 1
        ALUSrc = 1      # Use immediate
        MemWrite = 0
        ImmSrc = 4      # U-type
        ResultSrc = 0 
        ALUControl = 0b0010

    else:
        raise SimulatorError("Unsupported instruction")

def get_controls():
    return {
        "PCSrc" : PCsrc,
        "ResultSrc" : ResultSrc,
        "MemWrite" : MemWrite,
        "ALUControl" : ALUControl,
        "ALUSrc" : ALUSrc,
        "ImmSrc" : ImmSrc,
        "RegWrite" : RegWrite,
    }