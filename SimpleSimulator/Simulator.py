from memory import read_memory, write_memory
from error import SimulatorError
from register import read_register, write_register
from program_counter import getPC, PCnext, PCjump

try:
    write_memory(0x100, 4, 0x12345678)

    a = read_memory(0x100, 4)
    print(a)

    write_register(31, a)
    print(read_register(31))

    print(getPC())
    PCnext()
    print(getPC())
    PCjump(20)
    print(getPC())

except SimulatorError as e:
    print(e)