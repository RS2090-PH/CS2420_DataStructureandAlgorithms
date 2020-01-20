"""
Author: Robby Stohel
File: search.py

A program to compare run times for three types of searches:
    - Linear Search
    - Recursive Binary Search
    - Jump Search
"""
from time import perf_counter
from random import seed, sample
from recursioncounter import RecursionCounter

def linear_search(lyst, target):
    """
    Searches ordered list using the linear search algorithm.
    Process:
        Checks the first lyst value against the target value.
        If equal, true is returned. If not equal, the for loop
        shifts to the second value in the list and compares.
        This process repeats and returns true for a match, or
        false if the end is reached without a match.
    Args:
        lyst(list): The sorted list to be searched
        target(int): The value to be found
    Returns:
        bool: Returns True if the target is present
                and False if not found.
    """
    if not isinstance(target, int):
        raise ValueError("Target value must be an integer.")
    for step in lyst:
        if not isinstance(step, int):
            raise ValueError("List values must be integers.")
    if target < 0:
        raise ValueError("Target value must be a positive integer.")

    length = len(lyst)
    for rep in range(0, length):
        if lyst[rep] == target:
            return True
    return False

def recursive_binary_search(lyst, target):
    """
    Searches ordered list usint the recursive binary search algorithm.
    Process:
        Recieves the necessary values, creates the low
        and high values, then calls the recursive method
        using all the necessary data.
    Args:
        lyst(list): The sorted list to be searched
        target(int): The value to be found
    Returns:
        recursive_binary_search_helper(method): Returns the
        response provided by the recursive function. True
        if a match is found, and false otherwise.
    """
    if not isinstance(target, int):
        raise ValueError("Target value must be an integer.")
    for step in lyst:
        if not isinstance(step, int):
            raise ValueError("List values must be integers.")
    if target < 0:
        raise ValueError("Target value must be a positive integer.")
    low = 0
    high = len(lyst) -1

    return recursive_binary_search_helper(low, high, lyst, target)

def recursive_binary_search_helper(low_index, high_index, lyst, target):
    """
    Recursive function to search provided list.
    Process:
        If middle of list equals target value the middle value
        is returned. If the target is less than the middle value
        the method is recursively called with the range between
        the low and middle. If the target is greater than the
        middle, the method is recursively called with the range
        between the middle+1 and high values.
    Args:
        low_index(int): Lowest position in list search range
        high_index(int): Highest position in list search range
        lyst(list): The sorted list to be searched
        target(int): The value to be found
    Returns:
        bool: Returns True if the target is present
                and False if not found.
    """
    RecursionCounter()
    mid = (low_index + high_index) // 2

    if target > lyst[high_index]:
        return False

    if len(lyst) <= 0:
        return False

    if target == lyst[mid]:
        return True
    elif target < lyst[mid]:
        return recursive_binary_search_helper(low_index, mid, lyst, target)
    elif target > lyst[mid]:
        return recursive_binary_search_helper((mid + 1), high_index, lyst, target)

def jump_search(lyst, target):
    """
    Searches ordered list using the jump search algorithm.
    Process:
        Verifies the incrementer isn't greater than the total
        list count. If it is, the incrementer is decrimented to
        the last value in the list, then checked on whether that
        value is greater or less than the target. Greater returns
        false, less finds the value. If the counter is less than
        the count, the value at the cound potion is compared to
        the target and incremented ten places right if less than
        the target.
    Args:
        lyst(list): The sorted list to be searched
        target(int): The value to be found
    Returns:
        bool: Returns True if the target is present
                and False if not found.
    """
    if not isinstance(target, int):
        raise ValueError("Target value must be an integer.")
    for step in lyst:
        if not isinstance(step, int):
            raise ValueError("List values must be integers.")
    if target < 0:
        raise ValueError("Target value must be a positive integer.")

    length = len(lyst)
    incr = 0

    for rep in range(1, length):
        if incr >= length:
            incr = (incr - (incr - length)) - 1
            if lyst[incr] == target:
                return True
            elif target < lyst[incr]:
                for ret in range(1, 10):
                    if lyst[incr - ret] == target:
                        return True
            else:
                return False
        else:
            if target == lyst[incr]:
                return True
            elif lyst[incr] < target:
                incr += 10
            elif target < lyst[incr]:
                for ret in range(1, 10):
                    if lyst[incr - ret] == target:
                        return True

def main():
    """
    Main driver to test methods.
    Process:
        Calls each method, starting a timer before the call, then
        stopping the timer after completion to determine run time.
        Prints recorded data to the console.
    Args:
        Void
    Returns:
        Void
    """
    test_val = 10000000
    val_range = range(0, test_val)

    print("Creating a sorted array of %8d" % (test_val))
    seed(3)
    test_array = sample(val_range, k=test_val)
    test_array.sort()
    print("Finished creating a sorted array of %8d" % (test_val))
    print("")

    print("Searching for a number at the start of the array")
    start_time = perf_counter()
    result = linear_search(test_array, 5)
    run_time = perf_counter() - start_time
    print("        linear_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = recursive_binary_search(test_array, 5)
    run_time = perf_counter() - start_time
    print("        recursive_binary_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = jump_search(test_array, 5)
    run_time = perf_counter() - start_time
    print("        jump_search() returned {} in {} seconds".format(result, run_time))

    print("Searching for a number in the middle of the array")
    start_time = perf_counter()
    result = linear_search(test_array, 5000000)
    run_time = perf_counter() - start_time
    print("        linear_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = recursive_binary_search(test_array, 5000000)
    run_time = perf_counter() - start_time
    print("        recursive_binary_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = jump_search(test_array, 5000000)
    run_time = perf_counter() - start_time
    print("        jump_search() returned {} in {} seconds".format(result, run_time))


    print("Searching for a number at the end of the array")
    start_time = perf_counter()
    result = linear_search(test_array, test_val)
    run_time = perf_counter() - start_time
    print("        linear_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = recursive_binary_search(test_array, test_val)
    run_time = perf_counter() - start_time
    print("        recursive_binary_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = jump_search(test_array, test_val)
    run_time = perf_counter() - start_time
    print("        jump_search() returned {} in {} seconds".format(result, run_time))


    print("Searching for a number NOT in the array")
    start_time = perf_counter()
    result = linear_search(test_array, 50000000)
    run_time = perf_counter() - start_time
    print("        linear_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = recursive_binary_search(test_array, 50000000)
    run_time = perf_counter() - start_time
    print("        recursive_binary_search() returned {} in {} seconds".format(result, run_time))
    start_time = perf_counter()
    result = jump_search(test_array, 50000000)
    run_time = perf_counter() - start_time
    print("        jump_search() returned {} in {} seconds".format(result, run_time))
    print("")

if __name__ == "__main__":
    main()
