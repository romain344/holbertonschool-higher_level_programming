#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for a in range(x):
        try:
            if type(my_list[a]) == int:
                print("{:d}".format(my_list[a]), end="")
                count += 1
        except IndexError:
            break
    print()
    return count
