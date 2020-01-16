""" Checks a list then returns the position of the target item if found, or -1 otherwise. """

def sequential_search(target, lyst):
    """ Returns the position of the target item if found, or -1 otherwise. """
    position = 0

    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1

def main():
    """ Driver to test the function. """
    lyst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    sequential_search(7, lyst)

if __name__ == "__main__":
    main()
    