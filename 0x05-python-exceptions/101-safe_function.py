#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        answer = fct(*args)
    except Exception as avellin:
        print("Exception: {}".format(avellin), file=sys.stderr)
        return (None)
    else:
        return (answer)
