#!/usr/bin/python3
from sys import argv
total = 0
a = len(argv)
for i in range(1, a):
    total += int(argv[i])
else:
    print(total)
