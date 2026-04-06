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

    opcode = instruction & 0x3F
    funct3 = instruction & 0x7000
    funct7 = instruction & 0xFE000000


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