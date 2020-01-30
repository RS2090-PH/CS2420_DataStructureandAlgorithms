"""
File: palindrome.py
Project 7.2

"""

from arraystack import ArrayStack

def isPalindrome(string):          
    """Returns True if string is a palindrome
    or False otherwise."""
    stack1 = ArrayStack()
    stack2 = ArrayStack()

    for rep in range(0, len(string) - 1):
        stack1.push(string[rep])
    for rep in range(len(string) - 1, 0, -1):
        stack2.push(string[rep])

    if stack1 == stack2:
        return True
    else:
        return False

def main():
    while True:
        string = input("Enter a string or Return to quit: ")
        if string == "":
            break
        elif isPalindrome(string):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")

if __name__ == '__main__': 
    main()
