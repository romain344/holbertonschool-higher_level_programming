#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for a in my_string:
        if a != 'c' and a != 'C':
            string += a
    return string