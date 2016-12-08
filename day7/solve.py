#from __future__ import division
import re


def is_abba(istr):
    patt = re.compile(r'(.)(.)\2\1')
    for i in re.findall(patt, istr):
        if i[0] == i[1]:
            continue
        else: return True
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


    #print(is_abba('ioxxoj'))

    cnt = sum ([int(is_ipv7(i)) for i in input])

    print([int(is_ipv7(i)) for i in input])
    print(cnt)