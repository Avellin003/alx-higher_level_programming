#!/usr/bin/python3
import sys

a = len(sys.argv) - 1
if (a == 0):
    print("0 argument.")
elif (a == 1):
    print(a, "argument: ")
else:
    print(a, "arguments: ")
for i in range(a):
    print("{}:".format(i + 1), (sys.argv[i + 1]))