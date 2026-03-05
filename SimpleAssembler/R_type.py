from instructions import INSTRUCTIONtoFUNCT3
from errors import AssemblerError
from registers import XtoBINARY

def handle_R_instructions(opcode, words):
    binary_instruction = ""
    if len(words) != 4:
        raise AssemblerError("Invalid number of operands for R-type instruction")
    try:
        rd = XtoBINARY[words[1]]
        r1 = XtoBINARY[words[2]]
        r2 = XtoBINARY[words[3]]
    except KeyError as e:
        raise AssemblerError(f"Invalid register name: {e}")
    if words[0] == "add":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['add'] +rd + opcode
    elif words[0] == "sub":
        binary_instruction = "0100000" + r2 + r1 +INSTRUCTIONtoFUNCT3['sub'] +rd  + opcode  
    elif words[0] == "sll":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['sll'] +rd  + opcode
    elif words[0] == "slt":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['slt'] +rd  + opcode
    elif words[0] == "sltu":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['sltu'] +rd  + opcode
    elif words[0] == "xor":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['xor'] +rd  + opcode
    elif words[0] == "srl":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['srl'] +rd  + opcode
    elif words[0] == "or":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['or'] +rd  + opcode
    elif words[0] == "and":
        binary_instruction = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['and'] +rd  + opcode
    else:
        raise AssemblerError(f"Invalid R-type instruction '{words[0]}'")  



    return binary_instruction