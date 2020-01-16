"""
File: reverse.py
Project 3.2
Defines a function to reverse the elements in a list.
Computational complexity:
"""

def reverse(lyst):
    """Reverses the elements in a list in linear time."""
    # Use indexes to the first and last element
    # and move them toward each other.
    count = len(lyst)
    pos = count - 1

    for rep in range(0, count):
        if pos <= rep:
            break
        else:
            swap(lyst, lyst[rep], lyst[pos])
            pos -= 1


def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    temp = lyst[x]
    lyst[x] = lyst[y]
    lyst[y] = temp
    
def main():
    """Tests with two lists."""
    lyst = list(range(4))
    reverse(lyst)
    print(lyst)
    lyst = list(range(3))
    reverse(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
    
