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
