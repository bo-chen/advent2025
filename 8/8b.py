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

def dist(p1, p2):
    xd = p1[0] - p2[0]
    yd = p1[1] - p2[1]
    zd = p1[2] - p2[2]

    return math.sqrt(xd * xd + yd * yd + zd * zd)


pairs = []
for i, p1 in enumerate(ps):
    for j, p2 in enumerate(ps):
        if j >= i:
            continue
        d = dist(p1, p2)
        pairs.append([d, iatos(p1), iatos(p2)])

pairs.sort()

# coord -> primary coord
cirs = {}
# primary coord -> [counter, coord0, coord1, ...]
conns = {}

allcon = len(ps)

for i in range(len(pairs)):
    d, p1, p2 = pairs[i]
    if p1 not in cirs and p2 not in cirs:
        cirs[p1] = p1
        cirs[p2] = p1
        conns[p1] = [2, p1, p2]

    if p1 in cirs and p2 not in cirs:
        c = cirs[p1]
        cirs[p2] = c
        conns[c] = [1 + conns[c][0]] + conns[c][1:] + [p2]
        if conns[c][0] == allcon:
            print(stoia(p1)[0] * stoia(p2)[0])
            exit(0)

    if p2 in cirs and p1 not in cirs:
        c = cirs[p2]
        cirs[p1] = c
        conns[c] = [1 + conns[c][0]] + conns[c][1:] + [p1]
        if conns[c][0] == allcon:
            print(stoia(p1)[0] * stoia(p2)[0])
            exit(0)

    # merge
    if p2 in cirs and p1 in cirs:
        c1 = cirs[p1]
        c2 = cirs[p2]

        if c2 == c1:
            continue

        for overwritep in conns[c2][1:]:
            cirs[overwritep] = c1

        conns[c1] = [conns[c1][0] + conns[c2][0]] + conns[c1][1:] + conns[c2][1:]
        del conns[c2]
        if conns[c1][0] == allcon:
            print(stoia(p1)[0] * stoia(p2)[0])
            exit(0)
