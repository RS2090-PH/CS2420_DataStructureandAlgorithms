"""
Author: Robby Stohel
File: sort.py

A program to compare run times for five types of sorts:
    - Selection Sort
    - Insertion Sort
    - Merge Sort
    - Quick Sort
    - Tim Sort
"""

from copy import deepcopy
from random import seed, sample
from time import perf_counter
from recursioncounter import RecursionCounter

def selection_sort(lyst):
    """
    Sorts list using Selection Sort.
    Process:
        Checks lyst type, returning value error if not of list type. Then
        moves from one end of list to the other, comparing and swapping as
        needed.
    Args:
        lyst(list): A list of integers, of list type.
    Returns:
        lyst_copy(list): A copy of the original list after sort,
            even though the original list is directly modified.
    """
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    lyst_copy = lyst
    pos = 0
    length = len(lyst_copy)

    while pos != length:
        for rep in range(0, length):
            if lyst_copy[pos] < lyst_copy[rep]:
                temp = lyst_copy[rep]
                lyst_copy[rep] = lyst_copy[pos]
                lyst_copy[pos] = temp
        pos += 1

    return lyst_copy

def insertion_sort(lyst):
    """
    Sorts list using Insertion Sort.
    Process:
        Checks lyst type, returning value error if not of list type.
        Creates a copied list with just the first value in the original
        list, then moves along the original list, comparing the selected
        value with all the values in the copied list, and inserting it
        into the copied list where necessary.
    Args:
        lyst(list): A list of integers, of list type.
    Returns:
        lyst_copy(list): A copy of the original list after sort,
            even though the original list is directly modified.
    """
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    lyst_copy = [lyst[0]]
    length = len(lyst)
    copy_length = len(lyst_copy)
    pos = 1

    while pos < length:
        for rep in range(copy_length):
            if lyst[pos] == lyst_copy[rep]:
                lyst_copy.insert(rep, lyst[pos])
                copy_length = len(lyst_copy)
                break
            elif lyst[pos] < lyst_copy[rep]:
                lyst_copy.insert(rep, lyst[pos])
                copy_length = len(lyst_copy)
                break
            else:
                pass
        if lyst[pos] > lyst_copy[-1]:
            lyst_copy.append(lyst[pos])
            copy_length = len(lyst_copy)
        pos += 1

    return lyst_copy



def mergesort(lyst):
    """
    Sorts list using Merge Sort.
    Process:
        Checks lyst type, returning value error if not of list type.
        Breaks this into halves till there is just one value in each list,
        then sorts the list as it merges the values back together till the
        original list is whole and sorted.
    Args:
        lyst(list): A list of integers, of list type.
    Returns:
        lyst(list): A copy of the original list after sort,
            even though the original list is directly modified.
    """
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    copy_buffer = list()
    for count in range(len(lyst)):
        copy_buffer.insert(count - 1, None)

    merge_sort_helper(lyst, copy_buffer, 0, len(lyst) - 1)
    return lyst

def merge_sort_helper(lyst, copy_buffer, low, high):
    """ Helper method for mergesort(). """
    RecursionCounter()
    if low < high:
        middle = (low + high) // 2
        merge_sort_helper(lyst, copy_buffer, low, middle)
        merge_sort_helper(lyst, copy_buffer, middle + 1, high)
        merge(lyst, copy_buffer, low, middle, high)

def merge(lyst, copy_buffer, low, middle, high):
    """ Helper method for merge_sort_helper(). """
    val1 = low
    val2 = middle + 1

    for val in range(low, high + 1):
        if val1 > middle:
            copy_buffer[val] = lyst[val2]
            val2 += 1
        elif val2 > high:
            copy_buffer[val] = lyst[val1]
            val1 += 1
        elif lyst[val1] < lyst[val2]:
            copy_buffer[val] = lyst[val1]
            val1 += 1
        else:
            copy_buffer[val] = lyst[val2]
            val2 += 1
    for val in range(low, high + 1):
        lyst[val] = copy_buffer[val]

def quicksort(lyst):
    """
    Sorts list using Quick Sort.
    Process:
        Checks lyst type, returning value error if not of list type.
        Takes a pivot and sorts all values lower to the left, and
        higher to the right. Then takes each list of values left/right
        and performs the same process till the list is sorted.
    Args:
        lyst(list): A list of integers, of list type.
    Returns:
        lyst(list): A copy of the original list after sort,
            even though the original list is directly modified.
    """
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    quicksort_helper(lyst, 0, len(lyst) - 1)
    return lyst

def quicksort_helper(lyst, left, right):
    """ Helper method for quicksort(). """
    RecursionCounter()
    if left < right:
        pivot_location = partition(lyst, left, right)
        quicksort_helper(lyst, left, pivot_location - 1)
        quicksort_helper(lyst, pivot_location + 1, right)

def partition(lyst, left, right):
    """ Helper method for quicksort_helper(). """
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    swap(lyst, right, boundary)
    return boundary

def swap(lyst, val1, val2):
    """ Helper method for partition(). """
    temp = lyst[val1]
    lyst[val1] = lyst[val2]
    lyst[val2] = temp

def is_sorted(lyst):
    """
    Checks list sorting.
    Process:
        Checks lyst type, returning value error if not of list type,
        then checks list values to verify they are integers. After
        that, each value of the list is checked with the next value
        to verify order.
    Args:
        lyst(list): A list of integers, of list type.
    Returns:
        True/False(Bool): Returns True if list is sorted and False
            if list is unsorted.
    """
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")
    for count in lyst:
        if not isinstance(count, int):
            raise ValueError("Provided list must be of list type.")

    for count in range(0, len(lyst) - 2):
        if lyst[count] > lyst[count + 1]:
            return False

    return True


def main():
    """ Main driver to test methods. """
    test_val = 5000
    val_range = range(0, test_val)
    seed(3)
    test_array = sample(val_range, k=test_val)

    copy_array = deepcopy(test_array)
    print("starting selection_sort")
    start_time = perf_counter()
    selection_sort(copy_array)
    run_time = perf_counter() - start_time
    print("selection_sort duration: {} seconds".format(run_time))
    print("")

    copy_array = deepcopy(test_array)
    print("starting insertion_sort")
    start_time = perf_counter()
    insertion_sort(copy_array)
    run_time = perf_counter() - start_time
    print("insertion_sort duration: {} seconds".format(run_time))
    print("")

    copy_array = deepcopy(test_array)
    print("starting mergesort")
    start_time = perf_counter()
    mergesort(copy_array)
    run_time = perf_counter() - start_time
    print("mergesort duration: {} seconds".format(run_time))
    print("")

    copy_array = deepcopy(test_array)
    print("starting quicksort")
    start_time = perf_counter()
    quicksort(copy_array)
    run_time = perf_counter() - start_time
    print("quicksort duration: {} seconds".format(run_time))
    print("")

    copy_array = deepcopy(test_array)
    print("starting timsort")
    start_time = perf_counter()
    copy_array.sort()
    run_time = perf_counter() - start_time
    print("timsort duration: {} seconds".format(run_time))
    print("")

if __name__ == "__main__":
    main()
