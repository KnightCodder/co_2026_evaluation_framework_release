from error import SimulatorError

def extending_sign(element, bit):
    MSB = (element >> (bit - 1)) & 1
    if MSB:
        element -= (1 << bit)
    return element

def ImmExt(inst: int, ImmSrc: int):
    if ImmSrc == 0:
        sliding_bit = inst >> 20
        masked_bits = sliding_bit & 0xFFF
        return extending_sign(masked_bits, 12)
    elif ImmSrc == 1:
        upper_bits = inst >> 25
        lower_bits = (inst >> 7) & 0x1F
        combined = (upper_bits << 5) | lower_bits
        return extending_sign(combined, 12)
    elif ImmSrc == 2:
        bit31      = (inst >> 31) << 12
        bit7       = ((inst >> 7) & 0x1) << 11
        bits25_30  = ((inst >> 25) & 0x3F) << 5
        bits8_11   = ((inst >> 8) & 0xF) << 1
        combined   = bit31 | bit7 | bits25_30 | bits8_11
        return extending_sign(combined, 13)
    elif ImmSrc == 3:
        bit31      = (inst >> 31) << 20
        bits12_19  = ((inst >> 12) & 0xFF) << 12
        bit20      = ((inst >> 20) & 0x1) << 11
        bits21_30  = ((inst >> 21) & 0x3FF) << 1
        combined   = bit31 | bits12_19 | bit20 | bits21_30
        return extending_sign(combined, 21)
    elif ImmSrc == 4:
        return inst & 0xFFFFF000
    else:
        raise SimulatorError("Invalid ImmSrc")