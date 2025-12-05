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

        ls.append(lstripped)

rs = []
i = 0
for i in range(len(ls)):
    l = ls[i]
    if l == "":
        break

    rs.append(stoia(l, "-"))

rs.sort()

mrs = []
lastr = rs[0]
for r in rs:
    if r[0] <= lastr[1] + 1:
        if r[1] >= lastr[1]:
            lastr = [lastr[0],r[1]]
    else:
        mrs.append(lastr)
        lastr = r

mrs.append(lastr)

t = 0
print(mrs)
for r in mrs:
    t += r[1] - r[0] + 1


print(t)

