import sys
from toBinary import convertToBinary, minification_and_labeling
from errors import AssemblerError

try:
    input_assembly_path = sys.argv[1]
except IndexError:
    print("input_assembly_path not given")
    sys.exit(1)

try:
    output_machine_code_path = sys.argv[2]
except IndexError:
    print("output_machine_code_path not given")
    sys.exit(1)

try:
    output_readable_path = sys.argv[3]
except IndexError:
    output_readable_path = ""

try:
    with open(input_assembly_path, 'r') as f:
        lines = f.readlines()
        m_l_lines = minification_and_labeling(lines)
        binary = convertToBinary(m_l_lines)
    
    with open(output_machine_code_path, 'w') as f:
        for line in binary:
            f.write(line + "\n")

    if not output_readable_path:
        sys.exit()

    from toBinary import labels
    with open(output_readable_path, 'w') as f:
        f.write("Labels : PC\n")
        for label, pc in labels.items():
            f.write(f"\t{label}\t:\t{pc}\n")
        f.write(f"\n{30*'='}\n\n")

        for bin, (line_no, pc, instruction) in zip(binary, m_l_lines):
            f.write(f"{f"0x{int(bin, 2):08x}"}\tPC: {pc}\t{str(instruction)}\n")

except FileNotFoundError:
    print("Input file is not found on path:", input_assembly_path)
except AssemblerError as e:
    print(e)
