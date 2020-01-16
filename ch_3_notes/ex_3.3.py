"""
File: expo.py
Project 3.3
Defines a function to raise a number to a given power.
"""

def expo(base, exponent):
    """Raises base to exponent."""
   # verify values are non-negative
    result = base
    count = exponent - 1

    if(base or exponent) < 0:
        return -1
    elif(exponent) == 0:
        return 1

    while count > 0:
        result = result * base
        count -= 1

    return result

def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    
