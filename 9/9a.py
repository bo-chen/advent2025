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

ps = []

for l in ls:
    ps.append(stoia(l))

ms = 0

for p1 in ps:
    for p2 in ps:
        if p1 == p2:
            continue
        s = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
        if s > ms:
            ms = s

print(ms)