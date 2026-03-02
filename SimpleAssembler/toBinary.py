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

ABItoX = {
    "zero": "x0",
    "ra": "x1",
    "sp": "x2",
    "gp": "x3",
    "tp": "x4",
    "t0": "x5",
    "t1": "x6",
    "t2": "x7",
    "s0": "x8",
    "fp": "x8",
    "s1": "x9",
    "a0": "x10",
    "a1": "x11",
    "a2": "x12",
    "a3": "x13",
    "a4": "x14",
    "a5": "x15",
    "a6": "x16",
    "a7": "x17",
    "s2": "x18",
    "s3": "x19",
    "s4": "x20",
    "s5": "x21",
    "s6": "x22",
    "s7": "x23",
    "s8": "x24",
    "s9": "x25",
    "s10": "x26",
    "s11": "x27",
    "t3": "x28",
    "t4": "x29",
    "t5": "x30",
    "t5": "x31",
}

def standard_line(words):
    new_words = []
    for word in words:
        if word in ABItoX.keys():
            new_words.append(ABItoX[word])
        else:
            new_words.append(word)
    return new_words
        

def convertToBinary(lines):
    for i, line in enumerate(lines):
        words = line.split()
        if not words:
            continue

        if words[0] not in INSTRUCTIONtoOPCODE.keys():
            print("error in line", i+1)
            return
        
        words = standard_line(words)

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