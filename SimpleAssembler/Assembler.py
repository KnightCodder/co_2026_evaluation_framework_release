import sys
from toBinary import convertToBinary, minification_and_labeling
from errors import AssemblerError

input_assembly_path = sys.argv[1]
output_machine_code_path = sys.argv[2]
output_readable_path = sys.argv[3]

try:
    with open(input_assembly_path, 'r') as f:
        lines = f.readlines()
        binary = convertToBinary(minification_and_labeling(lines))
    
    with open(output_machine_code_path, 'w') as f:
        for line in binary:
            f.write(line + "\n")
except FileNotFoundError:
    print("Input file is not found on path:", input_assembly_path)
except AssemblerError as e:
    print(e)
