from error import SimulatorError

registers = [0] * 32

registers[2] = 0x0000017C # stack pointer
registers[3] = 0x00010000 # global pointer

program_counter = 0

def read_register(reg: int):
    if reg < 0 or reg > 31:
        raise SimulatorError("invalid register address")
    return registers[reg]

def write_register(reg: int, value: int):
    if reg < 0 or reg > 31:
        raise SimulatorError("invalid register address")
    if value < 0 or value > 0xFFFFFFFE:
        raise SimulatorError("invalid register value")
    if reg != 0:
        registers[reg] = value
