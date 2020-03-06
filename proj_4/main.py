"""
Author: Robby Stohel
File: main.py

This file contains the in2post() and eval_postfix() methods used in the main() test driver.
"""

from stack import Stack

def in2post(expr):
    """
    Reformats an infix expression to a postfix expression.
    Process:
        Takes an infix expression as an input and returns an equivalent postfix expression as
        a string. If the expression is not valid, raise a SyntaxError. If the parameter expr
        is not a string, raise a ValueError.
    Args:
        expr(Str): An infix, str-type expression
    Returns:
        A postfix, str-type expression
    """

    temp = expr
    stack = Stack()
    postfix = Stack()
    priority = {'^':1, '*':2, '/':2, '+':3, '-':3}

    if isinstance(temp, str) is False:
        raise ValueError("Expression must be in string format.")

    count = 0
    for char in temp:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
    if count != 0:
        raise SyntaxError("Not a valid expression")

    for char in temp:
        if char in ('\n', ' '):
            pass
        elif char == ')':
            while stack.peek() != '(':
                postfix.push(stack.pop())
            stack.pop()
        elif char == '(':
            stack.push(char)
        elif char in priority:
            if stack.size() == 0:
                stack.push(char)
            elif priority.get(stack.peek()) == priority.get(char):
                postfix.push(stack.pop())
                stack.push(char)
            elif stack.peek() != '(' and priority.get(stack.peek()) < priority.get(char):
                while stack.size() > 0:
                    if stack.peek() != '(':
                        postfix.push(stack.pop())
                    else:
                        break
                stack.push(char)
            else:
                stack.push(char)
        else:
            postfix.push(char)

    if stack.size() != 0:
        while stack.size() != 0:
            postfix.push(stack.pop())

    return postfix.__str__()

def eval_postfix(expr):
    """
    Evaluates postfix expression.
    Process:
        takes a postfix string as input and returns a number. If the
        expression is not valid, raise a SyntaxError.
    Args:
        expr(Str): A postfix, string expression
    Returns:
        A float-type expression solution
    """
    temp = expr
    stack = Stack()

    if isinstance(temp, str) is False:
        raise ValueError("Expression must be in string format.")

    try:
        for char in temp:
            if char == ' ':
                continue
            if char == '^':
                second = stack.pop()
                first = stack.pop()
                stack.push(first ** second)
            elif char == '*':
                stack.push(stack.pop() * stack.pop())
            elif char == '/':
                second = stack.pop()
                first = stack.pop()
                stack.push(first / second)
            elif char == '+':
                stack.push(stack.pop() + stack.pop())
            elif char == '-':
                second = stack.pop()
                first = stack.pop()
                stack.push(first - second)
            else:
                stack.push(int(char))
    except:
        raise SyntaxError("Not a valid expression")

    return float(stack.pop())

def main():
    """
    Main driver to run program.
    Process:
        -open file data.txt
        -read an infix expression from the file
        -display the infix expression
        -call function in2post(expr)
        -display the postfix expression
        -call function eval_postfix(expr)
        -display the result of eval_postfix()
    Args:
        None
    Returns:
        None
    """

    file = open("data.txt", "r")
    data = list()
    for line in file:
        data.append(line)
    file.close()

    for item in data:
        print("infix: ", item, end="")
        print("postfix: ", in2post(item))
        print("answer: ", eval_postfix(in2post(item)))
        print()

        print("2+5*7^2")
        print("matt's postfix: ", in2post("2+5*7^2"))

if __name__ == "__main__":
    main()
