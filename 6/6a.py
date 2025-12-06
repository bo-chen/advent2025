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
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

ns = []
i = 0
for i in range(len(ls) - 1):
    ns.append(stoia(ls[i],r"\s+"))

t = 0
i = 0
for op in re.split(r"\s+", ls[len(ls)-1]):
    st = 0
    if op == "*":
        st = 1

    for n in ns:
        if op == "+":
            st += n[i]
        else:
            st = st * n[i]

    t += st
    i += 1

print(t)
