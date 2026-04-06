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

    elif opcode == 0x63:
        RegWrite = 0
        ALUSrc = 0
        MemWrite = 0
        ImmSrc = 2

        if funct3 == 0x0:   # beq
            ALUControl = 0b0110

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