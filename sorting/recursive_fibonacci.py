"""  """

def fib(n):
    """ The recursive Fibonacci function. """
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    """  """
    print(fib(6))

if __name__ == "__main__":
    main()
