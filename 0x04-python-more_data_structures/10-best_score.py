#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_score = float("-inf")
    for key, value in a_dictionary.items():
        if not isinstance(value, int):
            raise TypeError("Dictionary can only contain integer values")
        if value > best_score:
            best_score = value
            best_key = key
    return best_key
