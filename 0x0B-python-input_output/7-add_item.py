#!/usr/bin/python3
"""module"""
import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args = sys.argv
file_name = "add_item.json"
# can also use os.path.exists(file) for try and except
# be sure to import os.path

try:
    json_list = load_from_json_file(file_name)
except Exception:
    json_list = []
for item in args[1:]:
    json_list.append(item)

save_to_json_file(json_list, file_name)
