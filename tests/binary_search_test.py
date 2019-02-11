import unittest
from solutions import binary_search

class BinarySearchTest(unittest.TestCase):
  def test_returns_false_if_empty_list(self):
    self.assertFalse(binary_search.is_present([], 1))

  def test_returns_false_if_item_missing1(self):
    self.assertFalse(binary_search.is_present([2], 1))

  def test_returns_false_if_item_missing2(self):
    self.assertFalse(binary_search.is_present([2, 3], 1))

  def test_returns_false_if_item_missing3(self):
    self.assertFalse(binary_search.is_present([2, 3, 4], 1))

  def test_returns_true_if_item_present1(self):
    self.assertTrue(binary_search.is_present([1], 1))

  def test_returns_true_if_item_present2(self):
    self.assertTrue(binary_search.is_present([1, 2], 1))

  def test_returns_true_if_item_present3(self):
    self.assertTrue(binary_search.is_present([1, 2, 3], 1))

  def test_returns_true_if_item_present4(self):
    self.assertTrue(binary_search.is_present([1, 2, 3], 2))

  def test_returns_true_if_item_present5(self):
    self.assertTrue(binary_search.is_present([1, 2, 3], 3))

  def test_returns_true_if_item_present6(self):
    self.assertTrue(binary_search.is_present([1, 2, 3, 4], 1))

  def test_returns_true_if_item_present7(self):
    self.assertTrue(binary_search.is_present([1, 2, 3, 4], 2))

  def test_returns_true_if_item_present8(self):
    self.assertTrue(binary_search.is_present([1, 2, 3, 4], 3))

  def test_returns_true_if_item_present9(self):
    self.assertTrue(binary_search.is_present([1, 2, 3, 4], 4))
