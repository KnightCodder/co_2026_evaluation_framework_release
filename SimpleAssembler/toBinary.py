from R_type import handle_R_instructions
from I_type import handle_I_instructions
from S_type import handle_S_instructions
from B_type import handle_B_instructions
from U_type import handle_U_instructions
from J_type import handle_J_instructions
from re import split as resplit, match as rematch
from registers import ABItoX, XtoBINARY
from instructions import INSTRUCTIONtoOPCODE, OPCODEStoINSTRUCTIONTYPE

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
    line_number = 1
    for line in lines:
        line = line.strip()
        if line:
            line = standard_line(resplit(r'[ ,]+', line.replace(':', ' : ').strip()))
            line_wo_labels = []
            for i in range(len(line)):
                line_wo_labels.append(line[i])
                if line[i] != ':':
                    continue
                if i == 0 or not(is_valid_label(line[i-1])) or line[i-1] in labels.keys():
                    print("error in line", line_number)
                    return
                labels[line[i-1]] = pc
                line_wo_labels.pop()
                line_wo_labels.pop()
                
            if line_wo_labels:
                code.append(line_wo_labels)
                pc += 4

        line_number += 1
    return code

def convertToBinary(lines):
    print(labels)

    for i, words in enumerate(lines):
        print(i, words)
        if words[0] not in INSTRUCTIONtoOPCODE.keys():
            print("error in line", i+1)
            return
        
        opcode = INSTRUCTIONtoOPCODE[words[0]]
        type = OPCODEStoINSTRUCTIONTYPE[opcode]

        binary = ""

        if type == "R":
            binary = handle_R_instructions(opcode, words)
        elif type == "I":
            binary = handle_I_instructions(opcode, words)
        elif type == "S":
            binary = handle_S_instructions(opcode, words)
        elif type == "B":
            binary = handle_B_instructions(opcode, words, labels)
        elif type == "U":
            binary = handle_U_instructions(opcode, words)
        elif type == "J":
            binary = handle_J_instructions(opcode, words, labels)
        else:
            print("error in convertToBinary function")
            return
        
        print(binary)
    