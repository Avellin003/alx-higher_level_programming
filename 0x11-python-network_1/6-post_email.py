#!/usr/bin/python3
"""Displays the header"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as ans:
        print(dict(ans.headers).get("X-Request-Id"))
