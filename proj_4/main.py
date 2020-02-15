"""
Author: Robby Stohel
File: main.py

This file contains the in2post() and eval_postfix() methods used in the main() test driver.
"""

from stack import Stack

def in2post(expr):
    #FIXME: call function in2post(expr) which you write in2post() takes an infix expression
    # as an input and returns an equivalent postfix expression as a string. If the expression
    # is not valid, raise a SyntaxError. If the parameter expr is not a string, raise a ValueError.
    return print("Return Value")

def eval_postfix(expr):
    #FIXME: call function eval_postfix(expr) which you write eval_postfix() takes a postfix string
    # as input and returns a number. If the expression is not valid, raise a SyntaxError.
    return print("Return Value")

def main():
    print("Temp Line")
    #FIXME:  open file data.txt 
    file = open("data.txt", "r")
    data = list()
    for line in file:
        data.append(line)
    file.close()

    #FIXME:  read an infix expression from the file 

    #FIXME:  display the infix expression 

    #FIXME:  call function in2post(expr) which you write in2post() takes an 
    # infix expression as an input and returns an equivalent postfix expression 
    # as a string. If the expression is not valid, raise a SyntaxError. If the parameter expr is not a string, raise a ValueError. 

    #FIXME:  display the postfix expression 

    #FIXME:  call function eval_postfix(expr) which you write eval_postfix() takes a postfix string as input and 
    # returns a number. If the expression is not valid, raise a SyntaxError. 

    #FIXME:  display the result of eval_postfix() 


if __name__ == "__main__":
    main()
