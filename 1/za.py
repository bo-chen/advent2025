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

lines = []
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            lines.append(lstripped)

x = 50
i = 0
for line in lines:
    print(line)
    if line[0] == "R":
        x = x + int(line[1:])
        x = x % 100
    if line[0] == "L":
        x = x - int(line[1:])
        x = x % 100

    print(x)
    if x == 0:
        i = i + 1

print(i)


