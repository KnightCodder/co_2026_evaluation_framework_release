import sys
from toBinary import convertToBinary

input_assembly_path = sys.argv[1]
output_machine_code_path = sys.argv[2]
output_readable_path = sys.argv[3]

try:
    with open(input_assembly_path, 'r') as f:
        lines = f.readlines()
        convertToBinary(lines)
except FileNotFoundError:
    print("Input file is not found on path:", input_assembly_path)
