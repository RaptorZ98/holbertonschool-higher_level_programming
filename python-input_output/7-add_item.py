#!/usr/bin/python3
""" add item """


import sys
sjf = __import__('5-save_to_json_file').save_to_json_file
ljf = __import__('6-load_from_json_file').load_from_json_file


try:
    list = ljf("add_item.json")
except FileNotFoundError:
    list = []

sjf(list + sys.argv[1:], "add_item.json")
