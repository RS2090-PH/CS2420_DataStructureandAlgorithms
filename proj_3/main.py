"""
Author: Robby Stohel
File: main.py

This module contains the main driver to test the CourseList
and Course classes.
"""

from courselist import CourseList
from course import Course

def main():
    """ Main driver to test CourseList and Course modules. """
    file = open("data.txt", "r")
    current_list = CourseList()
    for line in file:
        temp = line.split(",")
        current_list.insert(Course(int(temp[0]), str(temp[1]), float(temp[2]), float(temp[3])))
    file.close()

    print(current_list)

if __name__ == "__main__":
    main()
