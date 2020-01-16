""" Function to swap values. """

def swap(lyst, i, j):
    """ Exchanges the items at positions i and j. """
    # you could say ly[i], lyst[j] = lyst[j, lyst[i]
    # but the following code shows what is really happening.
    # This function usually needs an if statement to compare
    # and swap if necessary, then move the i and j valuse
    # to the next values in the list.

    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

#def main():
    # Currently unnecessary.


#if __name__ == "__main__":
#    main()
    