import math
# import numpy as np
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

cur = 50
t = 0
for l in ls:
    lastcur = cur
    n = int(l[1:])
    zeroes = 0
    if l[0] == "L":
        n = n * -1

    cur = cur + n
    if l[0] == "L":
        zeroes += int(cur / 100) * -1
        if cur <= 0 and lastcur > 0:
            zeroes += 1
    else:
        zeroes += int(cur / 100)

    cur = cur % 100
    #print(f"cur {str(cur)}, zeroes {str(zeroes)}")
    t += zeroes


print(t)



