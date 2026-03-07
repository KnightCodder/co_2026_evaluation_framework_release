from errors import AssemblerError
from registers import XtoBINARY
from instructions import INSTRUCTIONtoFUNCT3, INSTRUCTIONTYPEtoINSTRUCTIONS
from utils import immediate_to_integer, decimal_to_binary

def handle_B_instructions(opcode, words, PC, labels : dict):
    binary_instruction = ""

    if len(words) != 4:
        raise AssemblerError("Invalid number of operands for B-type instruction")

    instruction = words[0]
    rs1 = words[1]
    rs2 = words[2]

    if rs1 not in XtoBINARY.keys():
        raise AssemblerError(f"invalid source register name '{rs1}'")
    if rs2 not in XtoBINARY.keys():
        raise AssemblerError(f"invalid source register name '{rs2}'")

    if instruction in INSTRUCTIONTYPEtoINSTRUCTIONS["B"]:
        offset = 0
        if words[3] in labels.keys():
            offset = labels[words[3]] - PC
        else:
            try:
                offset = immediate_to_integer(imm=words[3], max_bits=13)
            except Exception as e:
                raise AssemblerError(e)
        if offset % 4:
            raise AssemblerError(f"target PC '{PC+offset}' is not a multiple of 4, hence invalid.")
        
        try:
            bin_offset = decimal_to_binary(offset // 2, 13)
        except Exception as e:
            raise AssemblerError(f'offset {e}')

        binary_instruction += bin_offset[0]
        binary_instruction += bin_offset[2:8]
        binary_instruction += XtoBINARY[rs2]
        binary_instruction += XtoBINARY[rs1]
        binary_instruction += INSTRUCTIONtoFUNCT3[instruction]
        binary_instruction += bin_offset[8:12]
        binary_instruction += bin_offset[1]
        binary_instruction += opcode

    else:
        raise AssemblerError(f"Unknown instruction '{instruction}'")

    return binary_instruction