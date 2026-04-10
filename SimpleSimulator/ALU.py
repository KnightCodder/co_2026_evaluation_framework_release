from error import SimulatorError

def ALU(SrcA: int, SrcB: int, ALUControl: int):
    mask=0xFFFFFFFF
    if ALUControl==0b0010:  
        return (SrcA+SrcB) &mask
    elif ALUControl==0b0110:  
        return (SrcA-SrcB) &mask
    elif ALUControl==0b0011: 
        return (SrcA<<(SrcB&0x1F)) &mask 
    elif ALUControl==0b0100: 
        a_sign=(SrcA & mask)-0x100000000 if(SrcA & 0x80000000) else(SrcA & mask)
        b_sign=(SrcB & mask)-0x100000000 if(SrcB & 0x80000000) else(SrcB & mask)
        return 1 if a_sign<b_sign else 0
    elif ALUControl==0b0101: 
        a = SrcA & 0xFFFFFFFF
        b = SrcB & 0xFFFFFFFF
        return 1 if a < b else 0
    elif ALUControl==0b0111: 
        return SrcA^SrcB
    elif ALUControl==0b1000: 
        return ((SrcA & mask) >> (SrcB & 0x1F)) & mask
    elif ALUControl==0b0001: 
        return SrcA|SrcB
    elif ALUControl==0b0000: 
        return SrcA&SrcB
    elif ALUControl == 0b1010:  # LUI (Pass-through SrcB)
        return SrcB & mask
    else:
        raise SimulatorError("invalid ALU control")
