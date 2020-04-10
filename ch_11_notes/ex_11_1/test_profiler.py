import unittest
from hashtable import HashTable
from profiler import Profiler


class UnitTests(unittest.TestCase):
  def test_get_collisions(self):
    table = HashTable(8, lambda x: x)
    data = range(10, 71, 10)
    profiler = Profiler()
    profiler.test(table, data)
    self.assertEqual(profiler.getCollisions(), 3)

  def test_get_prove_count1(self):
    table = HashTable(8, lambda x: x)
    data = range(10, 71, 10)
    profiler = Profiler()
    profiler.test(table, data)
    self.assertEqual(profiler.getProbeCount(), 3)

  def test_len(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(len(table), 7)

  def test_str(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(str(table), "[40, None, 10, 50, 20, 60, 30, 70]")

  def testget_load_factor(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.getLoadFactor(), 0.875)

  def test_get_home_index(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.getHomeIndex(), 6)

  def test_get_actual_index(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.getActualIndex(), 7)

  def test_get_probe_count2(self):
    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    self.assertEqual(table.getProbeCount(), 1)
