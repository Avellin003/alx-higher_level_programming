#!/usr/bin/python3
"""SENDS A REQUEST TO A GIVEN URL"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as ans:
            print(ans.read().decode("UTF-8"))
    except urllib.error.HTTPError as i:
        print("Error code: ", i.code)
