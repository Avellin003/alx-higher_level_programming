#!/usr/bin/python3
"""write script that adds to python list"""
from sys import argv as ar
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json(filename)
except FileNotfoundError:
    json_list = []

for i in ar[1:]:
    json_list.append(ar)

save_to_json_file(json_list, filename)
