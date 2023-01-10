#!/usr/bin/python3
"""module"""
import json
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file_name = "add_item.json"

try:
    json_list = load_from_json_file(file_name)
except Exception:
    json_list = []
for item in argv[1:]:
    json_list.extend(item)

save_to_json_file(json_list, file_name)
