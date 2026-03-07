from R_type import handle_R_instructions
from I_type import handle_I_instructions
from S_type import handle_S_instructions
from B_type import handle_B_instructions
from U_type import handle_U_instructions
from J_type import handle_J_instructions
from re import split as resplit, match as rematch
from registers import ABItoX
from instructions import INSTRUCTIONtoOPCODE, OPCODEStoINSTRUCTIONTYPE
from errors import AssemblerError

labels = dict()

def standard_line(words):
    new_words = []
    for word in words:
        if word in ABItoX.keys():
            new_words.append(ABItoX[word])
        else:
            new_words.append(word)
    return new_words

def is_valid_label(label):
    return rematch(r'^[A-Za-z_][A-Za-z0-9_]*$', label) is not None

def minification_and_labeling(lines):
    code = []
    pc = 0
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if line:
            line = standard_line(resplit(r'[ ,()]+', line.replace(':', ' : ').strip()))
            line_wo_labels = []
            for i in range(len(line)):
                if not line[i]:
                    continue
                line_wo_labels.append(line[i])
                if line[i] != ':':
                    continue
                if i == 0 or not(is_valid_label(line[i-1])) or line[i-1] in labels.keys():
                    raise AssemblerError(line_no=line_number, message=f"Invalid Label '{line[i-1]}'")
                labels[line[i-1]] = pc
                line_wo_labels.pop()
                line_wo_labels.pop()
                
            if line_wo_labels:
                code.append((line_number, pc, line_wo_labels))
                pc += 4
    return code

def convertToBinary(lines):
    print(labels)
    binary_lines = []

    for line_number, pc, words in lines:
        print(line_number, pc, words)
        if words[0] not in INSTRUCTIONtoOPCODE.keys():
            raise AssemblerError(line_no=line_number, message="Invalid instruction")
        
        opcode = INSTRUCTIONtoOPCODE[words[0]]
        type = OPCODEStoINSTRUCTIONTYPE[opcode]

        binary = ""

        try:
            if type == "R":
                binary = handle_R_instructions(opcode, words)
            elif type == "I":
                binary = handle_I_instructions(opcode, words)
            elif type == "S":
                binary = handle_S_instructions(opcode, words)
            elif type == "B":
                binary = handle_B_instructions(opcode, words, pc, labels)
            elif type == "U":
                binary = handle_U_instructions(opcode, words)
            elif type == "J":
                binary = handle_J_instructions(opcode, words, pc, labels)
            else:
                raise AssemblerError(message="convertToBinary function not working properly.")
        except AssemblerError as e:
            raise AssemblerError(line_no=line_number, message=e)
        
        binary_lines.append(binary)
    
    return binary_lines
    