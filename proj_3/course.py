"""
Author: NAME
File: FILE

DESCRIPTION
"""

class Course(object):
    """
    QuickDescription.
    Process:
        FullProcessDescription.
    Args:
        Argument(Type): ArgDescription
    Returns:
        ReturnValue(Type): ReturnDescription
    """
    def __init__(self, num = 0, crs = "", cred = 0.0, gra = 0.0, next = None):
        self.c_num = int(num)
        self.crs = str(crs)
        self.cred = float(cred)
        self.gra = float(gra)
        self.next = next

    def __str__(self):
        return str(self.c_num) + " " + str(self.crs) + " Grade: " + str(self.gra) + " Credit Hours: " + str(self.cred)

    def number(self):
        """ Space holder """
        return self.c_num

    def name(self):
        """ Space holder """
        return self.crs

    def credit_hr(self):
        """ Space holder """
        return self.cred

    def grade(self):
        """ Space holder """
        return self.gra
    
def main():
    """ To test list """

    head = None
    head = Course(1400, "Introduction to Programming", 4, 3.6, head)
    head = Course(1410, "C++ Programming", 4, 2.6, head)
    head = Course(2810, "Computer Architecture", 3, 3.8, head)

    print(head)
    head = head.next
    print(head)
    head = head.next
    print(head)

    print(head.number())
    print(head.name())
    print(head.credit_hr())
    print(head.grade())

if __name__ == "__main__":
    main()