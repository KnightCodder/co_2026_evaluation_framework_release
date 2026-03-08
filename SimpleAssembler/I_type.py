from instructions import INSTRUCTIONtoFUNCT3
from errors import AssemblerError
from registers import XtoBINARY
from utils import decimal_to_binary
from utils import immediate_to_integer

def handle_I_instructions(opcode, words):
    binary_instruction = ""
    if words[0] != "lw":
        if len(words) != 4:
            raise AssemblerError("Invalid number of operands for I-type instruction")
        try:
            rd =  XtoBINARY[words[1]]
            rs1 = XtoBINARY[words[2]]
            imm = words[3]
            imm = immediate_to_integer(imm, 12)
            imm = decimal_to_binary(imm, 12)

        except KeyError as e:
            raise AssemblerError(f"Invalid register name: {e}")
        except Exception as e:
            raise AssemblerError(e)
        if words[0] == "addi":
            binary_instruction = imm + rs1 + INSTRUCTIONtoFUNCT3['addi'] + rd + opcode
        elif words[0] == "sltiu":
            binary_instruction = imm + rs1 + INSTRUCTIONtoFUNCT3['sltiu'] + rd + opcode
        elif words[0] == "jalr":
            binary_instruction = imm + rs1 + INSTRUCTIONtoFUNCT3['jalr'] + rd + opcode
        else:
            raise AssemblerError(f"Invalid I-type instruction '{words[0]}'")

    elif words[0] == "lw":
        if len(words) != 4:
            raise AssemblerError("Invalid number of operands for lw instruction")
        try:
            rd = XtoBINARY[words[1]]
            imm = words[2]
            imm = immediate_to_integer(imm, 12)
            imm = decimal_to_binary(imm, 12)
            rs1 = words[3]
            rs1 = XtoBINARY[rs1]

        except KeyError as e:
            raise AssemblerError(f"Invalid register name: {e}")
        except Exception as e:
            raise AssemblerError(e)
        
        binary_instruction = imm + rs1 + INSTRUCTIONtoFUNCT3['lw'] + rd + opcode
        
    

    return binary_instruction