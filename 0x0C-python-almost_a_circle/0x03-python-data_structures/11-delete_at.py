#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list.remove(idx + 1)
        return my_list
