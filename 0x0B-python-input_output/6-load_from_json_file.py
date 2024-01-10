#!/usr/bin/python3
"""Defines a fubction for reading JSON files"""
import json


def load_from_json_file(filename):
    """Construct a Python object by using a JSON file"""
    with open(filename) as f:
        return json.load(f)
