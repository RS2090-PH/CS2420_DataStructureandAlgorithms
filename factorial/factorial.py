""" CS2420 in class example """

def factorial(value):
    """ returns value!, value must be an integer or raise ValueError """
    if not isinstance(value, int):
        raise ValueError("value must be an integer")
    if value < 0:
        raise ValueError("value must be non-negative")
    # base case
    if value <= 1:
        return 1

    # recusive case
    return value * factorial(value - 1)

# in cmd
# python -m pylint factorial.py
# python -m unittest test_factorial.py
# use cls in terminal to clear it
# pass this into the command line when running the file
# to test the coding structure (score of -10 - 10)

def main():
    """ driver to test factorial """
    try:
        #print(factorial("6"))    This is to test passing in a string for the ValueError
        print(factorial(6))
    except ValueError as err:
        print("Oops", err)

if __name__ == "__main__":
    main()
