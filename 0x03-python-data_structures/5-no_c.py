#!/usr/bin/env python3
def no_c(my_string):
    string = my_string
    for i in my_string:
        if i != 'c' and i != 'C':
            return ("".join(string))
