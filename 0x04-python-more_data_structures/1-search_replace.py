#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for idx, p to enumerate(new_list):
        if p == search:
            new_list[idx] = replace
    return new_list
