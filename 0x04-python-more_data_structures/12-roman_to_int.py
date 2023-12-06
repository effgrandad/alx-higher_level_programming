#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dgit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    for h in range(len(roman_string)):
        if h > 0 and roman_dgit[roman_string[h]] > roman_dgit[roman_string[h - 1]]:
            roman_num += roman_dgit[roman_string[h]] - 2 * \ roman_dgit[roman_string[h + 1]]
        else:
            roman_num += roman_dgit[roman_string[h]]
    return roman_num
