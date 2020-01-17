"""
Project 3.9
File: testquicksort.py

Tests the quicksort algorithm
"""

import random

def insertionSort(lyst, left, right):
    i = left + 1
    while i < right + 1:
        item_to_insert = lyst[i]
        j = i - 1

        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = item_to_insert
        i += 1

def quicksort(lyst):
    if len(lyst) < 50:
        insertionSort(lyst, 0, len(lyst) - 1)
    else:
        quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def main(size = 20, sort = quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)

    lyst2 = [6, 4, 8, 2]
    sort(lyst2)
    print(lyst2)

if __name__ == "__main__":
    main() 
