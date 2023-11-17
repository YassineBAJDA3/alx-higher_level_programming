#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    i = sum(score * wight for score, wight in my_list)
    j = sum(weight for _, weight in my_list)

    if j == 0:
        return 0

    return i / j
