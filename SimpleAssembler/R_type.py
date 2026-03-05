from instructions import INSTRUCTIONtoFUNCT3
from errors import AssemblerError
from registers import XtoBINARY

def handle_R_instructions(opcode, words):
    binary_instruction = ""
    if len(words) != 5:
        raise AssemblerError("Invalid number of operands for R-type instruction")
    rd = XtoBINARY(words[1])
    r1 = XtoBINARY(words[2])
    r2 = XtoBINARY(words[3])
    if words[0] == "add":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['add'] +rd + "000" + opcode
    elif words[0] == "sub":
        func = "0100000" + r2 + r1 +INSTRUCTIONtoFUNCT3['sub'] +rd + "000" + opcode  
    elif words[0] == "sll":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['sll'] +rd + "000" + opcode
    elif words[0] == "slt":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['slt'] +rd + "000" + opcode
    elif words[0] == "sltu":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['sltu'] +rd + "000" + opcode
    elif words[0] == "xor":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['xor'] +rd + "000" + opcode
    elif words[0] == "srl":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['srl'] +rd + "000" + opcode
    elif words[0] == "or":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['or'] +rd + "000" + opcode
    elif words[0] == "and":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['and'] +rd + "000" + opcode
    else:
        raise AssemblerError(f"Invalid R-type instruction '{words[0]}'")  



    return binary_instruction