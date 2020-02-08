import unittest
from ermodel import Condition, Patient, ERModel


class UnitTests(unittest.TestCase):
    def schedule_test(self):
        er = ERModel()
        p1 = Patient("John", 2)

        er.schedule(p1)
        self.assertFalse(er.patients.isEmpty())

    def add_test(self):
        er = ERModel()
        p1 = Patient("John", 2)

        self.assertTrue(er.isEmpty())
        er.patients.add(p1)
        self.assertFalse(er.isEmpty())

    def treat_test(self):
        er = ERModel()
        p1 = Patient("John", 2)
        p2 = Patient("Sally", 1)

        er.patients.add(p1)
        er.patients.add(p2)
        self.assertTrue(er.treatNext() == p2)
        self.assertTrue(er.treatNext() == p1)
        self.assertTrue(er.treatNext() == None)
