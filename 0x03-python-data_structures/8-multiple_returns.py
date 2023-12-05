#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    initiative_char = sentence[0] if length > 0 else "None"
    tup = length, initiative_char
    return (tup)
