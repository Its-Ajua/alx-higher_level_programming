#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divVal = a / b
    except (TypeError, ZeroDivisionError):
        divVal = None
    finally:
        print("Inside result: {}".format(divVal))
    return (divVal)
