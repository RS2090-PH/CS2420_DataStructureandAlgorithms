"""
Author: Robby Stohel
File: course.py

This module contains the Course class for creating and modifying
Course objects.
"""

class Course():     # Removed "object" as pylint advises python3+ doesn't need it.
    """ Course class to create individual course objects. """
    def __init__(self, num=0, crs="", cred=0.0, gra=0.0):
        """ Course object initializer. """
        if isinstance(num, int) is not True or num < 0:
            raise ValueError("Course ID must be an integer.")
        if crs is None:
            raise ValueError("Course Name cannot be None.")
        if isinstance(cred, (int, float)) is not True or cred < 0:
            raise ValueError("Course Credits must be an integer or float.")
        if isinstance(gra, (int, float)) is not True or gra < 0:
            raise ValueError("Course Credits must be a positive integer or float.")
        self.c_num = num
        self.crs = crs
        self.cred = cred
        self.gra = gra
        self.next = None

    def __str__(self):
        """ Provides a string representation of Course objects. """
        return "%s %s Grade:%1.1f Credit Hours: %1.1f"%(self.c_num, self.crs, self.gra, self.cred)

    def number(self):
        """ Returns the course number. """
        return self.c_num

    def name(self):
        """ Returns the course name. """
        return self.crs

    def credit_hr(self):
        """ Returns the credit hour amount. """
        return self.cred

    def grade(self):
        """ Returns the grade point value. """
        return self.gra
