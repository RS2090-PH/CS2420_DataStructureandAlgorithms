"""
File: fib.py
Project 3.6

Employs memoization to improve the efficiency of recursive Fibonacci.
"""

def fib(n, table):
    """Fibonacci function with a table for memoization."""
    if n in table:
        return table[n]
        
    else:
        # Attempt to get values for n - 1 and n - 2
        # from the table
        # If unsuccessful, recurse and add results to
        # the table

        if n < 3:
            return 1
        else:
            table[n] = fib(n - 1, table) + fib(n - 2, table)
            return table[n]


def main():
    """Tests the function with some powers of 2."""
    problemSize = 2
    print("%4s%12s" % ("n", "fib"))
    for count in range(5):
        print("%4d%12d" % (problemSize, fib(problemSize, {})))
        problemSize *= 2

        print(fib(3,{}))
        print(fib(6,{}))
        print(fib(12,{}))
        print(fib(24,{}))
        print(fib(48,{}))


if __name__ == "__main__":
    main()
