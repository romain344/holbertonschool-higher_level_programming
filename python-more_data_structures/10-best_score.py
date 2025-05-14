#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary) > 0:
        return max(a_dictionary, key=a_dictionary.get)
    return None