#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    nume = 0
    deno = 0
    for i in my_list:
        nume += i[0] * i[1]
        deno += i[1]
    return (nume / deno)
