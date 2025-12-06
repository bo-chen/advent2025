import math
import os
import re
import sys
import copy
from functools import *
from pathlib import Path

source_path = Path(__file__).resolve()
source_dir = source_path.parent

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

def cpm(m):
    return [r[:] for r in m]

def stoia(pstr, delim = ","):
    return list(map(lambda x: int(x), re.split(delim,pstr.strip())))

def iatos(p):
    return ",".join(map(lambda x: str(x), p))

ls = []
maxll = 0
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        if len(line) > maxll:
            maxll = len(line)
        ls.append(line)


nls = ls[:-1]

def calc(op, s, e):
    st = 0
    if op == "*":
        st = 1
    elif op != "+":
        print(f"{op} {int(s)} {int(e)}")
        print("bad")
        exit(0)

    for i in range(s, e):
        s = ""
        for l in nls:
            if i >= len(l):
                s = s + " "
            else:
                s = s + l[i]

        if s.strip()== "":
            continue

        if op == "*":
            st = st * int(s)
        else:
            st = st + int(s)

    return st

lastop = ""
lastopi = 0
t= 0
for i,c in enumerate(ls[len(ls)-1][:-1]):
    if i == 0:
        lastop = c
        continue

    if c != "+" and c != "*":
        continue

    t += calc(lastop, lastopi, i)
    lastopi = i
    lastop = c

t += calc(lastop, lastopi, maxll)

print(t)
