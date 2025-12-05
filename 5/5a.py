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

    b, e = l.split("-")
    rs.append([int(b), int(e)])

t = 0
print(i)
i+=1
while i < len(ls):
    n = int(ls[i])
    for r in rs:
        if r[0] <= n <= r[1]:
            t += 1
            break

    i += 1

print(t)
