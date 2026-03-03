from SimpleAssembler.instructions import INSTRUCTIONtoOPCODE
from SimpleAssembler.utils import immediate_to_integer
from SimpleAssembler.utils import decimal_to_binary
from errors import AssemblerError
from registers import XtoBINARY

def handle_S_instructions(opcode, words):

    binary_instruction = ""
    instruction = words[0]
    reg_imm=words[2].strip(")")
    reg_imm=words[2].split("(")
    rs1=reg_imm[1]
    if rs1 not in XtoBINARY.keys():
        raise AssemblerError(f"wrong source register name '{rs1}'")
    imm = reg_imm[0]
    imm=immediate_to_integer(imm, 12)
    imm=decimal_to_binary(imm, 12)
    imm=str(imm)
    imm1=imm[0:7]
    imm2=imm[7:12]
    rd = words[1]
    if rd not in XtoBINARY.keys():
        raise AssemblerError(f"wrong destination register name '{rd}'")
    if instruction == "sw":
        instruction=INSTRUCTIONtoOPCODE["sw"]
    else:
        raise AssemblerError(f"wrong instruction name '{instruction}'")
    binary_instruction =imm1+ XtoBINARY[rs1] + XtoBINARY[rd] + imm2 + instruction
    return binary_instruction