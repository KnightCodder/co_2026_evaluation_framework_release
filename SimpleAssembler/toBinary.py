from R_type import handle_R_instructions
from I_type import handle_I_instructions
from S_type import handle_S_instructions
from B_type import handle_B_instructions
from U_type import handle_U_instructions
from J_type import handle_J_instructions

OPCODEStoINSTRUCTIONTYPE = {
    "0110011": "R",
    "0100011": "S",
    "1100011": "B",
    "1101111": "J",
    "0110111": "U",
    "0010111": "U",
    "0010011": "I",
    "0000011": "I",
    "1100111": "I"
}

INSTRUCTIONtoOPCODE = {
    "add": "0110011",
    "sub": "0110011",
    "sll": "0110011",
    "slt": "0110011",
    "sltu": "0110011",
    "xor": "0110011",
    "srl": "0110011",
    "or": "0110011",
    "and": "0110011",

    "addi": "0010011",
    "sltiu": "0010011",

    "lw": "0000011",

    "jalr": "1100111",

    "sw": "0100011",

    "beq": "1100011",
    "bne": "1100011",
    "blt": "1100011",
    "bge": "1100011",
    "bltu": "1100011",
    "bgeu": "1100011",

    "lui": "0110111",

    "auipc": "0010111",

    "jal": "1101111",
}

def convertToBinary(lines):
    for i, line in enumerate(lines):
        words = line.split()
        if not words:
            continue

        if words[0] not in INSTRUCTIONtoOPCODE.keys():
            print("error in line", i+1)
            return
        
        opcode = INSTRUCTIONtoOPCODE[words[0]]
        type = OPCODEStoINSTRUCTIONTYPE[opcode]

        binary = ""

        if type == "R":
            binary = handle_R_instructions(opcode, words)
        elif type == "I":
            binary = handle_I_instructions(opcode, words)
        elif type == "S":
            binary = handle_S_instructions(opcode, words)
        elif type == "B":
            binary = handle_B_instructions(opcode, words)
        elif type == "U":
            binary = handle_U_instructions(opcode, words)
        elif type == "J":
            binary = handle_J_instructions(opcode, words)
        else:
            print("error in convertToBinary function")
            return
        
        print(binary)