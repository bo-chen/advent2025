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
    return list(map(lambda x: int(x), pstr.strip().split(delim)))

def iatos(p):
    return ",".join(map(lambda x: str(x), p))

ls = []
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

t = 0
for r in ls[0].split(","):
    [s, e] = r.split("-")
    for n in range(int(s),int(e) + 1):
        sn = str(n)
        l = len(sn)
        if len(sn) % 2 == 0:
            if sn[:int(l/2)] == sn[int(l/2):]:
                t += n


print(t)



