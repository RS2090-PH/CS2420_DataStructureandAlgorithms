""" Searches a list for the minimum value and prints its index. """

def index_of_min(lyst):
    """ Returns the index of the minimum item. """
    min_index = 0
    current_index = 1

    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index

def main():
    """ Main driver to test function. """
    lyst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1]

    print(index_of_min(lyst))

if __name__ == "__main__":
    main()
