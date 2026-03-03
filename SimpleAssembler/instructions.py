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

INSTRUCTIONtoFUNCT3 = {
    "beq": "000",
    "bne": "001",
    "blt": "100",
    "bge": "101",
    "bltu": "110",
    "bgeu": "111",
    "sw" : "010",
}

INSTRUCTIONTYPEtoINSTRUCTIONS = {
    "R": ("add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"),
    "I": ("addi", "sltiu", "lw", "jalr"),
    "S": ("sw",),
    "B": ("beq", "bne", "blt", "bge", "bltu", "bgeu",),
    "U": ("lui", "auipc",),
    "J": ("jal",),
}