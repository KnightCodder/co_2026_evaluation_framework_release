from errors import AssemblerError
from registers import XtoBINARY
from utils import immediate_to_integer, decimal_to_binary

def handle_J_instructions(opcode, words, PC, labels : dict):
    binary_instruction = ""

    instruction = words[0]
    rd = words[1]
    if rd not in XtoBINARY.keys():
        raise AssemblerError(f"wrong destination register name '{rd}'")

    if instruction == "jal":
        offset = 0
        if words[2] in labels.keys():
            offset = labels[words[2]] - PC
        else:
            try:
                offset = immediate_to_integer(imm=words[2], max_bits=21)
            except Exception as e:
                raise AssemblerError(e)
        if offset % 4:
            raise AssemblerError(f"target PC '{PC+offset}' is not a multiple of 4, hence invalid.")
        
        try:
            bin_offset = decimal_to_binary(offset // 2, 21)
        except Exception as e:
            raise AssemblerError(f'offset {e}')
        
        # print(bin_offset)
        
        binary_instruction += bin_offset[0]
        binary_instruction += bin_offset[10:20]
        binary_instruction += bin_offset[9]
        binary_instruction += bin_offset[1:9]

        binary_instruction += XtoBINARY[rd]
        binary_instruction += opcode

    else:
        raise AssemblerError(f"Unknown instruction '{instruction}'")

    return binary_instruction