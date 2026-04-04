from error import SimulatorError

program_counter = 0

def getPC():
    return program_counter

def PCnext():
    global program_counter
    program_counter += 4

def PCjump(newPC: int):
    if newPC % 4 != 0:
        raise SimulatorError("invalid PC value")
    global program_counter
    program_counter = newPC
    