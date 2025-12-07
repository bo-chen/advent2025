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
            ls.append(list(lstripped))

t = 0
def beam(i, j):
    global t
    if i < 0 or i > len(ls[0]) or j >= len(ls):
        return 1
    if ls[j][i] == "|":
        return 0

    if ls[j][i] == ".":
        ls[j][i] = "|"
        return beam(i, j+1)

    if ls[j][i] == "^":

        t += 1
        return beam(i-1,j) + beam (i+1, j)

    print("bad")
    print(ls[j][i])
    exit(0)


for i, c in enumerate(ls[0]):
    if c == "S":
        break

print(beam(i, 1))
print(t)


