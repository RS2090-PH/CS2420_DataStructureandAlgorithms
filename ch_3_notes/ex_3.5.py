"""
File: sort.py
Project 3.5
Allows the user to specify the direction of a selection sort.
"""

def selectionSort(lyst, reverse = False):
    """Sorts the list items in ascending order if
    reverse is False; otherwise, sorts 'em in
    descending order."""
    if not reverse:
        # Sort in ascending order, counting up
        i = 0

        while i < len(lyst) - 1: # This loop iterates through the list till all values are compared
            min_index = i
            j = i + 1

            while j < len(lyst): # This loop does the comparison
                if lyst[j] < lyst[min_index]:
                   min_index = j
                j += 1
            if min_index != i:
                swap(lyst, min_index, i)
            i += 1

    else:
        # Sort in descending order, counting down
        i = 0

        while i < len(lyst) - 1: # This statement iterates through the list till all values are compared
            min_index = i
            j = i + 1

            while j < len(lyst): # This statement does the comparison
                if lyst[j] > lyst[min_index]:
                   min_index = j
                j += 1
            if min_index != i:
                swap(lyst, min_index, i)
            i += 1

def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    temp = lyst[x]
    lyst[x] = lyst[y]
    lyst[y] = temp

def main():
    """Tests with four lists."""
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst)
    print(lyst)
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst, reverse = True)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst, reverse = True)
    print(lyst)

if __name__ == "__main__":
    main()
