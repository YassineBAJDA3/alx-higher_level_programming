#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    my_listdiv = []
    for i in my_list:
        if (i % 2) == 0:
            my_listdiv.append(True)
        else:
            my_list-div.append(False)
    return my_listdiv
