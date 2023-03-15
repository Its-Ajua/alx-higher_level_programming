#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    curr = 0
    total = 0

    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    for i in range(len(roman_string)):
        curr = rom_num[roman_string[i]]
        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total += curr

        prev = curr
    return (total)
