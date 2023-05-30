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
    with open(fname, 'arrr') as file:
        MyList = json.load(file)
except:
    pass

for i in range(1, len(sys.argv)):
    MyList.append(sys.argv[i])
save_to_json_file(MyList, fname)
