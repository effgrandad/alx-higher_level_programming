#!/usr/bin/python3
"""Defines a function for writing JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Write a JSON representation of an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
