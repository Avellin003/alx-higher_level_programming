#!/usr/bin/python3
"""Fetches url"""

import requests

if __name__ == "__main__":
    req = request.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: ", type(req.text))
    print("\t- content: ", (req.text))
