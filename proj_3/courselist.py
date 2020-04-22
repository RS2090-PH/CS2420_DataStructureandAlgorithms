"""
Author: Robby Stohel
File: courselist.py

This module contains the CourseList class for creating and modifying
CourseList objects.
"""

from recursioncounter import RecursionCounter

class CourseList():     # Removed "object" as pylint advises python3+ doesn't need it.
    """ CourseList class to create grouped course objects. """
    def __init__(self, head=None):
        """ CourseList object initializer. """
        self.head = head
        self.list_size = 0
        self.probe = None

    def __str__(self):
        """ Provides a string representation of CourseList objects. """
        temp = ""
        temp += "Current List: (%d)\n"%(self.size())
        for item in self:
            temp += ("cs" + str(item) + "\n")
        temp += "\n\n\n"
        temp += "Cumulative GPA: %1.3f"%(round(self.calculate_gpa(), 3))
        temp += "\n\n"

        return temp

    def __iter__(self):
        """ Provides an iterable CourseList object. """
        def recurse(node):
            """ Recursive helper for the iterator. """
            if node is not None:
                temp.append(node)
                recurse(node.next)

        temp = list()
        probe = self.head
        recurse(probe)

        return iter(temp)

    def __next__(self):
        """ Returns the next Course object in the CourseList. """
        probe = self.head
        if probe is None:
            return None
        if probe.next is None:
            probe = self.head

        probe = probe.next
        return probe

    def insert(self, course):
        """ Inserts a course object into the CourseList. """

        if self.head is None:
            course.next = self.head
            self.head = course
            self.list_size += 1
            return self.head

        if course.number() < self.head.number():
            course.next = self.head
            self.head = course
            self.list_size += 1
            return self

        def recurse(trail, probe, course):
            """ Recursive helper for inserting Course objects. """
            _ = RecursionCounter()
            if probe is None:
                course.next = probe
                trail.next = course
                self.list_size += 1
                return self
            if trail.number() < course.number() < probe.number():
                course.next = probe
                trail.next = course
                self.list_size += 1
                return self

            return recurse(probe, probe.next, course)

        probe = self.head
        return recurse(probe, probe.next, course)

    def remove(self, number):
        """ Removes courses based on course number. """
        if self.head is None:
            return -1
        if self.head.number() == number:
            self.head = self.head.next
            return self
        if self.head.number() != number \
            and self.head.next is None:
            return -1

        def recurse(trail, node, number):
            """ Recusive helper for removing courses. """
            _ = RecursionCounter()
            if node is None:
                return -1
            if node.number() == number:
                trail.next = node.next
                self.list_size -= 1
                return self
            return recurse(node, node.next, number)

        probe = self.head.next
        trail = self.head
        return recurse(trail, probe, number)

    def remove_all(self, number):
        """ Removes all instances of a course. """
        def recurse(number):
            """ Recursive helper for removing multiple courses. """
            if self.remove(number) != -1:
                recurse(number)
            return self
        return recurse(number)

    def find(self, number):
        """ Returns desired course based on course number. """
        probe = self.head
        if probe is None:
            return -1
        if probe.number() == number:
            return probe

        def recurse(node, number):
            """ Recursive helper for finding course. """
            _ = RecursionCounter()
            if node is None:
                return -1
            if node.number() == number:
                return node
            return recurse(node.next, number)

        return recurse(probe.next, number)

    def size(self):
        """ Returns the size of the current CourseList. """
        count = 0
        probe = self.head

        if self.head is None:
            return count

        def recurse(node, count):
            """ Recursive helper to determine CourseList size. """
            _ = RecursionCounter()
            if node is not None:
                count += 1
                return recurse(node.next, count)
            return count

        return recurse(probe, count)

    def calculate_gpa(self):
        """ Calculates cumulative gpa based on all courses. """
        if self.head is None:
            return 0.0

        def recurse(node, grades, credit_hrs):
            """ Recursive helper to build cumulative gpa value. """
            _ = RecursionCounter()
            if node is None:
                return grades / credit_hrs
            return recurse(node.next, grades + (node.grade() * node.credit_hr()),\
                credit_hrs + node.credit_hr())

        probe = self.head
        return recurse(probe.next, (probe.grade() * probe.credit_hr()), probe.credit_hr())

    def is_sorted(self):
        """ Verifies CourseList is sorted. """
        probe = self.head

        def recurse(node, next_val):
            """ Recursive helper to verify sort. """
            _ = RecursionCounter()
            if next_val is not None:
                if next_val.number() > node.number():
                    recurse(next_val, next_val.next)
                elif next_val.number() < node.number():
                    return False
            return True

        if self.head is None:
            return True

        return recurse(probe, probe.next)
