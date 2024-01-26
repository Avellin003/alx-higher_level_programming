#!/usr/bin/python3
"""SENDS A REQUEST TO A GIVEN URL"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as ans:
            print(ans.read().decode("ascii"))
    except urllib.error.HTTPError as i:
        print(f"Erro code: {e.code}")
