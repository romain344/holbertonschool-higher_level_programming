#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    
    max_value = my_list[0]
    for a in my_list:
        if a > max_value:
            max_value = a
    return max_value