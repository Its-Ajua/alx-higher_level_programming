#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict = list(a_dictionary.keys())
    a_dict.sort()
    for i in a_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
