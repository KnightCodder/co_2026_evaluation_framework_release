from error import SimulatorError

PCsrc = 0
ResultSrc = 0
MemWrite = 0
ALUControl = 0
ALUSrc = 0
ImmSrc = 0
RegWrite = 0

def decode_instruction(instruction: int):
    global PCsrc, ResultSrc, MemWrite, ALUControl, ALUSrc, ImmSrc, RegWrite



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