""" To show funtionality of the merge sort algorithm. """

import random
from arrays import Array
from swap import swap

def merge_sort(lyst):
    # lyst: list being sorted
    # copy_buffer: temporary space needed during merge
    copy_buffer = Array(len(lyst))
    merge_sort_helper(lyst, copy_buffer, 0, len(lyst) - 1)

def merge_sort_helper(lyst, copy_buffer, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sort_helper(lyst, copy_buffer, low, middle)
        merge_sort_helper(lyst, copy_buffer, middle + 1, high)
        merge(lyst, copy_buffer, low, middle, high)

def merge(lyst, copy_buffer, low, middle, high):
    """  """
    # lyst: list tha tis being softed
    # copy_buffer: temp space needed during the merge process
    # low: beginning of first sorted sublist
    # middle: end of first sorted sublist
    # middle +  1: beginning of second sorted sublist
    # high: end of second sorted sublist
    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1
    # Interleave  items from the sublists into the 
    # copy_buffer in such a way that order is maintained
    for i in range(low, high + 1):
        if i1 > middle:
            copy_buffer[i] = lyst[i2] # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copy_buffer[i] = lyst[i1] # Second sublist exhausted
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copy_buffer[i] = lyst[i1] # Item in first sublist <
            i1 += 1
        else:
            copy_buffer[i] = lyst[i2] # item in second sublist <
            i2 += 1
    for i in range(low, high + 1):  # Copy sorted items back to
        lyst[i] = copy_buffer[i]    # propert position in lyst

def main(size=20, sort=merge_sort):
    """  """
    lyst = []

    for count in range(size):
        lyst.append(random.randint(1, size + 1))

    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
