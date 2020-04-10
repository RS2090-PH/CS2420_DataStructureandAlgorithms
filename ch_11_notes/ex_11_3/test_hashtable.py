import unittest
from hashtable import HashTable

class UnitTests(unittest.TestCase):
  def test_get1(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.get(10), 2)
    self.assertEqual(table.get(20), 4)
    self.assertEqual(table.get(30), 6)

  def test_get2(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.get(99), -1)

  def test_remove1(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.remove(10), 2)
    self.assertEqual(str(table), "[40, None, True, 50, 20, 60, 30, 70]")
    self.assertEqual(table.remove(60), 5)
    self.assertEqual(str(table), "[40, None, True, 50, 20, True, 30, 70]")

  def test_remove2(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.remove(99), -1)
    self.assertEqual(str(table), "[40, None, 10, 50, 20, 60, 30, 70]")
