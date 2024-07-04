#!/usr/bin/python3
"""
Module: 6-peak

This module contains a function find_peak to find a peak in an unsorted list of integers.
A peak is defined as an element that is greater than or equal to its neighbors.

Functions:
- find_peak(list_of_integers): Finds a peak in the list of integers using a binary search-like approach.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in an unsorted list of integers.

    Args:
    - list_of_integers (list): List of integers to search for a peak.

    Returns:
    - Integer: A peak found in the list, or None if no peak is found.

    Complexity:
    - Time: O(log(n)), where n is the number of elements in the list.
    - Space: O(1), as only constant extra space is used.
    """

    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If left neighbor is greater, go left
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1

        # Otherwise, go right
        else:
            low = mid + 1

    return None
