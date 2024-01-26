#!/usr/bin/python3
"""Displays the header"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as ans:
        print(dict(an s.headers).get("X-Request-Id"))
