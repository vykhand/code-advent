import re

def get_modifier(msg):
    modif  = []
    s = ""
    while s != ")":
        s = msg.pop(0)
        modif.append(s)
    modif = "".join(modif)
    match  = re.match(r"(\d+)x(\d+)\)", modif)
    if match is not None:
        n_sym = match.group(1)
        mult = match.group(2)
        return int(n_sym), int(mult)
    else:
        raise ValueError("modifier has incorrect format")
    
def get_len(msg):
    
    msg = list(msg)
    
    l = 0
    
    while len(msg) > 0:
        s =  msg.pop(0)
        if s == "(":
            n_sym, mult = get_modifier(msg)
            msg = msg[n_sym:]
            l += n_sym*mult
        elif re.match(r"\s", s) is None:
            l += 1
    return l
    



if __name__ == "__main__":

    assert(get_len("ADVENT") == 6)
    assert(get_len("A(1x5)BC") == 7)
    assert(get_len("(3x3)XYZ") == 9)
    assert(get_len("A(2x2)BCD(2x2)EFG") == 11)
    assert(get_len("(6x1)(1x3)A") == 6)
    assert(get_len("X(8x2)(3x3)ABCY") == 18)


    with open('day9\input.txt', 'r') as f:
        msg = f.readline()
    print get_len(msg)

            
