def immediate_to_integer(imm : str, max_bits : int):
    try:
        i = int(imm, 0)
    except ValueError:
        raise Exception(f"Immediate '{imm}' is not a number.")
    low = -(2**(max_bits-1))
    high = (2**(max_bits-1))-1
    if i < low or i > high:
        raise Exception(f"Immediate '{i}' is not in range [{low}, {high}]")
    
    return i

def decimal_to_binary(dec : int, max_bits : int):
    low = -(2**(max_bits-1))
    high = (2**(max_bits-1))-1
    if dec < low or dec > high:
        raise Exception(f"'{dec}' is not in range [{low}, {high}]")
    
    if dec >= 0:
        return format(dec, f'0{max_bits}b')
    else:
        mask = (1 << max_bits) - 1
        return format(dec & mask, f'0{max_bits}b')
