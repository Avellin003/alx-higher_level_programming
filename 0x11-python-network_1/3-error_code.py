#!/usr/bin/python3
"""SENDS A REQUEST TO A GIVEN URL"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as ans:
            print(ans.read().decod('UTF-8'))
    except urllib.error.HTTPError as i:
        print("Error code: ", i.code)
