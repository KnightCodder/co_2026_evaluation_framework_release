from errors import AssemblerError
from registers import XtoBINARY
from utils import immediate_to_unsigned_integer, decimal_to_unsigned_binary

def handle_U_instructions(opcode, words):
    binary_instruction = ""

    if len(words) != 3:
        raise AssemblerError("Invalid number of operands for U-type instruction")

    instruction = words[0]
    rd = words[1]
    registers_key = XtoBINARY.keys()
    if rd not in registers_key:
        message_error = f"wrong register name '{rd}'"
        raise AssemblerError(message_error)
    imm = words[2]
    try:
        imm_int = immediate_to_unsigned_integer(imm, 20)
        imm_bin = decimal_to_unsigned_binary(imm_int, 20)
        imm = imm_bin

    except Exception as e:
        raise AssemblerError(e)

    binary_instruction = imm + XtoBINARY[rd] + opcode

    return binary_instruction