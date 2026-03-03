from logging import exception

from instructions import INSTRUCTIONtoFUNCT3, INSTRUCTIONtoOPCODE
from utils import immediate_to_integer
from utils import decimal_to_binary
from errors import AssemblerError
from registers import XtoBINARY

def handle_S_instructions(opcode, words):

    binary_instruction = ""
    instruction = words[0]
    rs1=words[3]
    if rs1 not in XtoBINARY.keys():
        raise AssemblerError(f"wrong source register name '{rs1}'")
    imm = words[2]
    try: 
        imm=immediate_to_integer(imm, 12)
        imm=decimal_to_binary(imm, 12)
    except Exception as e:
        raise AssemblerError(e)
    imm=str(imm)
    imm1=imm[0:7]
    imm2=imm[7:12]
    rd = words[1]
    func=INSTRUCTIONtoFUNCT3[instruction]
    if rd not in XtoBINARY.keys():
        raise AssemblerError(f"wrong destination register name '{rd}'")
    binary_instruction = imm1+ XtoBINARY[rd] + XtoBINARY[rs1] +func+ imm2 + opcode
    return binary_instruction