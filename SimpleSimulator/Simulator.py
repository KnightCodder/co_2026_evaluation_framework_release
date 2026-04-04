from memory import read, write
from error import SimulatorError

try:
    write(0x100, 4, 0x123456789)

    print(read(0x100, 4))
except SimulatorError as e:
    print(e)