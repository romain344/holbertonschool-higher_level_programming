#!/usr/bin/python3
"""défine la fonction"""


def divisible_by_2(my_list=[]):
    """vérifie si les éléments de la liste sont divisibles par 2"""
    result = []

    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
