#!/usr/bin/python3
"""
7-add_item
write a script that adds all arguments to a python list, then save to file
"""
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fname = "add_item.json"
MyList = []

try:
        data = load_from_json_file('add_item.json')
except:
    data = []

new_items = sys.argv[1:]
updated_data = data + new_items

save_to_json_file(updated_data, 'add_item.json')
