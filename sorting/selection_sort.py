""" To show funtionality of the selection sort algorithm. """
from basic_sort_algs import swap

def selection_sort(lyst):
    """ Takes first position and compares to whole list, swapping if necessary. Moves on to second position etc. """
    i = 0

    while i < len(lyst) - 1: # This statement iterates through the list till all values are compared
        min_index = i
        j = i + 1

        while j < len(lyst): # This statement does the comparison
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1

def main():
    """ Main driver to test function. """
    lyst = [6, 2, 4, 1, 8, 3, 5, 7, 9]

    print(lyst)
    selection_sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
        