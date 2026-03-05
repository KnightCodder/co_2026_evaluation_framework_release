from instructions import INSTRUCTIONtoFUNCT3
from errors import AssemblerError
from registers import XtoBINARY

def handle_R_instructions(opcode, words):
    binary_instruction = ""
    if len(words) != 4:
        raise AssemblerError("Invalid number of operands for R-type instruction")
    rd = XtoBINARY(words[1])
    r1 = XtoBINARY(words[2])
    r2 = XtoBINARY(words[3])
    if words[0] == "add":
        func = "0000000" + r2 + r1 +INSTRUCTIONtoFUNCT3['add'] +rd + "000" + opcode
    elif words[0] == "sub":
        func = "0100000" + r2 + r1 + rd + "000" + opcode    



    return binary_instruction