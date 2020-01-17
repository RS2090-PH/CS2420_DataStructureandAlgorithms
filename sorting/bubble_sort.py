""" Uses the bubble sort algorithm to sort a list. """

from swap import swap

def bubble_sort(lyst):
    """
    Compares two objects. If the left is more than
    the right they swap, otherwise the comparison moves
    over one place and begins again.
    """

    count = len(lyst)

    while count > 1: # Do n-1 bubbles
        i = 1   # Start each bubble

        while i < count:
            if lyst[i] < lyst[i - 1]: # Exchange if needed
                swap(lyst, i, i - 1)
            i += 1
        count -= 1

def main():
    """ Main driver to test function. """
    lyst = [6, 2, 4, 1, 8, 3, 5, 7, 9]

    print(lyst)
    bubble_sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
