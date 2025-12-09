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

vs = []
hs = []
def irs(p, lastp):
    global hs
    global vs
    if p[0] == lastp[0]:
        if p[1] >= lastp[1]:
            vs.append([[p[0],lastp[1]],[p[0],p[1]]])       
        else:
            vs.append([[p[0],p[1]], [p[0],lastp[1]]])
    elif p[1] == lastp[1]:
        if p[0] >= lastp[0]:
            hs.append([[lastp[0],p[1]], [p[0], p[1]]])       
        else:
            hs.append([[p[0],p[1]], [lastp[0],p[1]]])
    else:
        print("bad")
        exit(0)

lastp = None
for l in ls:
    p = stoia(l)
    ps.append(p)
    if lastp is not None:
        irs(p, lastp)
    lastp = p

irs(lastp, ps[0])

def checki(s1):
    if s1[0][0] == s1[1][0]:
        if s1[0][1] > s1[1][1]:
            s1 = [s1[1], s1[0]]
        for rp in hs:
            if s1[0][1] < rp[0][1] and \
                    rp[0][1] < s1[1][1] and \
                    rp[0][0] < s1[0][0] and \
                    s1[0][0] < rp[1][0]:
                return True
    elif s1[0][1] == s1[1][1]:
        if s1[0][0] > s1[1][0]:
            s1 = [s1[1], s1[0]]
        for rp in vs:
            if rp[0][1] < s1[0][1] and \
                    s1[0][1] < rp[1][1] and \
                    s1[0][0] < rp[0][0] and \
                    rp[0][0] < s1[1][0]:
                return True
    else:
        print("bad2")
        exit(1)

    return False
        

def checkborders(p1, p2):
    xs = sorted([p1[0],p2[0]])
    ys = sorted([p1[1],p2[1]])

    if checki([[xs[0],ys[0] + 0.1 ], [xs[1], ys[0] + 0.1]]) or\
            checki([[xs[1] - 0.1,ys[0]], [xs[1] - 0.1, ys[1]]]) or\
            checki([[xs[1],ys[1] - 0.1], [xs[0], ys[1] - 0.1]]) or\
            checki([[xs[0] + 0.1,ys[1]], [xs[0] + 0.1, ys[0]]]):
        return True

ms = 0

for p1 in ps:
    for p2 in ps:
        if p1 == p2:
            continue
        if not checkborders(p1, p2):
            s = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if s > ms:
                ms = s

print(ms)