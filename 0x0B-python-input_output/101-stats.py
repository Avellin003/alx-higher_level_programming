#!/usr/bin/python3
"""import of module"""
import sys

file_size = 0
status = {"200": 0, "301": 0, "400": 0, "401": 0, 
        "403": 0, "404": 0, "405": 0, "500": 0}
a = 0
try:
    for ln in sys.stdin:
        tok = ln.split()
        if len(tok) >= 2:
            b = a
            if tok[-2] in status:
                status[tok[-2]] += 1
                a += 1
            try:
                file_size += int(tok[-1])
                if b == a:
                    a += 1
            except FileNotFoundError:
                if b == i:
                    continue
            if a % 10 == 0:
                print("File size: {:d}".format(file_size))
                for k, v in sorted(status.items()):
                    if v:
                        print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for k, v in sorted(status.items()):
        if v:
            print("{:s}: {:d}".format(key, value))
