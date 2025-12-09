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

points = []

vsegs = []
hsegs = []
def irs(p, lastp):
    global hsegs
    global vsegs
    if p[0] == lastp[0]:
        if p[1] >= lastp[1]:
            vsegs.append([[p[0],lastp[1]],[p[0],p[1]]])       
        else:
            vsegs.append([[p[0],p[1]], [p[0],lastp[1]]])
    elif p[1] == lastp[1]:
        if p[0] >= lastp[0]:
            hsegs.append([[lastp[0],p[1]], [p[0], p[1]]])       
        else:
            hsegs.append([[p[0],p[1]], [lastp[0],p[1]]])
    else:
        print("bad")
        exit(0)

lastp = None
for l in ls:
    p = stoia(l)
    points.append(p)
    if lastp is not None:
        irs(p, lastp)
    lastp = p

irs(lastp, points[0])

def checkseginter(seg):
    if seg[0][0] == seg[1][0]:
        if seg[0][1] > seg[1][1]:
            seg = [seg[1], seg[0]]
        for hseg in hsegs:
            if seg[0][1] < hseg[0][1] and \
                    hseg[0][1] < seg[1][1] and \
                    hseg[0][0] < seg[0][0] and \
                    seg[0][0] < hseg[1][0]:
                return True
    elif seg[0][1] == seg[1][1]:
        if seg[0][0] > seg[1][0]:
            seg = [seg[1], seg[0]]
        for vseg in vsegs:
            if vseg[0][1] < seg[0][1] and \
                    seg[0][1] < vseg[1][1] and \
                    seg[0][0] < vseg[0][0] and \
                    vseg[0][0] < seg[1][0]:
                return True
    else:
        print("bad2")
        exit(1)

    return False
        

def checkbordersinter(p1, p2):
    xs = sorted([p1[0],p2[0]])
    ys = sorted([p1[1],p2[1]])

    if checkseginter([[xs[0],ys[0] + 0.1 ], [xs[1], ys[0] + 0.1]]) or\
            checkseginter([[xs[1] - 0.1,ys[0]], [xs[1] - 0.1, ys[1]]]) or\
            checkseginter([[xs[1],ys[1] - 0.1], [xs[0], ys[1] - 0.1]]) or\
            checkseginter([[xs[0] + 0.1,ys[1]], [xs[0] + 0.1, ys[0]]]):
        return True

ms = 0

for p1 in points:
    for p2 in points:
        if p1 == p2:
            continue
        if not checkbordersinter(p1, p2):
            s = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if s > ms:
                ms = s

print(ms)