from error import SimulatorError

program_memory_size = 64 * 4
stack_memory_size = 32 * 4
data_memory_size = 32 * 4

program_memory = [0] * program_memory_size
stack_memory = [0] * stack_memory_size
data_memory = [0] * data_memory_size

def decode_address(address: int):
    if address >= 0 and address <= 0xFF:
        return ("program", address)
    elif address >= 0x100 and address <= 0x17F:
        return ("stack", address - 0x100)
    elif address >= 0x10000 and address <= 0x1007F:
        return ("data", address - 0x10000)
    else:
        raise SimulatorError("invalid address")

def read_byte(address: int):
    try:
        code, adr = decode_address(address)
    except SimulatorError as e:
        raise SimulatorError(f"{e}: while trying to read memory")
    
    if code == "program":
        return program_memory[adr]
    elif code == "stack":
        return stack_memory[adr]
    else:
        return data_memory[adr]
    
def read_memory(address: int, bytes: int):
    res = 0
    for i in range(bytes-1, -1, -1):
        res <<= 8
        res += read_byte(address + i)
    return res

def write_byte(address: int, value: int):
    try:
        code, adr = decode_address(address)
    except SimulatorError as e:
        raise SimulatorError(f"{e}: while trying to write memory")
    
    if value < 0 or value > 0xFF:
        raise SimulatorError("value out of range while to trying to write")
    
    if code == "program":
        raise SimulatorError("trying to write into program memory")
    elif code == "stack":
        stack_memory[adr] = value
    else:
        data_memory[adr] = value

def write_memory(address: int, bytes: int, value: int):
    try:
        for adr in range(address, address+bytes):
            write_byte(adr, value & 0xFF)
            value >>= 8
    except SimulatorError as e:
        raise SimulatorError(e);

def fill_program_memory(binary: list[str]):
    address = 0
    for bin in binary:
        bin = bin.strip()
        if (bin):
            try:
                ibin = int(bin, 2)
            except ValueError:
                raise SimulatorError("Invalaid instruction")
            if address >= program_memory_size:
                raise SimulatorError("instructions too large")
            if ibin < 0 or ibin > 0xFFFFFFFF:
                raise SimulatorError("invalid instruction")
            
            for i in range(4):
                program_memory[address+i] = ibin & 0xFF
                ibin >>= 8
            address += 4

def memory_to_str():
    res = ""

    for i in range(0, data_memory_size, 4):
        bin = data_memory[i+3]
        bin <<= 8
        bin |= data_memory[i+2]
        bin <<= 8
        bin |= data_memory[i+1]
        bin <<= 8
        bin |= data_memory[i]
        res += f"0x{(0x10000+i):08X}" + ":" + f"0b{bin:032b}" + "\n"

    return res
    
def memory_to_str_readable():
    res = ""

    for i in range(0, data_memory_size, 4):
        bin = data_memory[i+3]
        bin <<= 8
        bin |= data_memory[i+2]
        bin <<= 8
        bin |= data_memory[i+1]
        bin <<= 8
        bin |= data_memory[i]
        res += f"0x{(0x10000+i):08X}" + ":" + f"0x{bin:08X}" + "\n"

    return res
    
