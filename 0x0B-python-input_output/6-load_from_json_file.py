#!/usr/bin/python3
"""imports json module"""
import json


def load_from_json_file(filename):
    """function that loads from json file"""
    with open(filname, encoding="utf-8") as a:
        return json.loads(a.read())
