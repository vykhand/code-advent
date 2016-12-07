#from __future__ import division
import re

def is_abba(instr):
    if len(instr) % 2 != 0:
        return False
    else:
        half_len = int(len(instr)/2)

    if instr[:half_len] == instr[half_len:][::-1] \
            and instr[:half_len] != instr[half_len:]:
        return True
    else:
        return False

def is_ipv7(ip):
    patt = re.compile(r'\[(\w+)\]')
    for i in re.findall(patt, ip):
        if is_abba(i):
            return False
    patt = re.compile(r'\[\w+\]')
    rest  = re.split(patt, ip)
    for i in rest:
        if is_abba(i):
            return True
    return False


if __name__ == "__main__":
    fname = "input.txt"
    with open("input.txt",'r') as f:
        input  =  f.readlines()

    cnt = sum ([int(is_ipv7(i)) for i in input])

    print([int(is_ipv7(i)) for i in input])