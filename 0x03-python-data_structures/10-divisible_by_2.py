#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divi = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            divi.append(True)
        else:
            divi.append(False)
    return (divi)
