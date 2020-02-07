"""
Author: NAME
File: FILE

DESCRIPTION
"""
from course import Course
from recursioncounter import RecursionCounter

class CourseList(Course):
    """
    QuickDescription.
    Process:
        FullProcessDescription.
    Args:
        Argument(Type): ArgDescription
    Returns:
        ReturnValue(Type): ReturnDescription
    """
    def __init__(self, head = None):
        self.head = head
        if head is not None:
            Course.__init__(self, head.c_num, head.crs, head.cred, head.gra, head.next)


    def __str__(self):
        """ Space holder """
        return str(self.c_num) + " " + str(self.crs) + " Grade: " + str(self.gra) + " Credit Hours: " + str(self.cred)


    def __iter___(self):
        """ Space holder """
        return self

    def __next__(self):
        """ Space holder """
        probe = self
        return probe.next

    def insert(self, course):
        """ Space holder """
        if self.head is None:
            CourseList.__init__(self, Course(course.c_num, course.crs, course.cred, course.gra))
        else:
            self.probe = self.head
            def course_viewer(course, probe):
                _ = RecursionCounter()
                if course.c_num < self.probe.c_num:
                    return course_viewer(Course(course.c_num, course.crs, course.cred, course.gra, probe), self.probe)
                else:
                    CourseList.__init__(self, Course(course.c_num, course.crs, course.cred, course.gra, probe))
            course_viewer(course, self.probe)


    def remove(self, number):
        """ Space holder """

    def remove_all(self, number):
        """ Space holder """


    def find(self, number):
        """ Space holder """

    def size(self, ):
        """ Space holder """

    def calculate_gpa(self, ):
        """ Space holder """

    def is_sorted(self):
        """ Space holder """

def main():
    """ To test list """
    head = CourseList()
    #head = CourseList(Course(1400, "Introduction to Programming", 4, 3.6))
    #head = CourseList(Course(1410, "C++ Programming", 4, 2.6, head))
    #head = CourseList(Course(2810, "Computer Architecture", 3, 3.8, head))

    head.insert(Course(1400, "Introduction to Programming", 4, 3.6))
    head.insert(Course(1410, "C++ Programming", 4, 2.6))
    head.insert(Course(2810, "Computer Architecture", 3, 3.8))

    #print(head)
    #head = head.next
    #print(head)
    #head = head.next
    print(head)
    #print(next(head))
    #print(next(head))
    print(head.next)
    print(head.next.next)
    #print(next(head))


    RecursionCounter.recursion_count = 0
    cl = CourseList()
    for i in range(1000, 1100):
        cl.insert(Course(i, "Test", 1.0, 1.0))
    print(RecursionCounter.recursion_count)
    print(cl)
    print(cl.next)
    print(cl.next.next)
    print(cl.next.next.next)

if __name__ == "__main__":
    main()
