"""
File: expo.py
Project 3.4

Defines a function to raise a number to a given power.
Computational complexity: O(n log n)
"""

def expo(base, exponent):
    """Raises base to exponent."""

    if exponent == 0:
        return 1
    elif exponent % 2 != 0:
        return base * expo(base, exponent - 1)
    else:
        response = expo(base, exponent / 2)
        return response * response

def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    
