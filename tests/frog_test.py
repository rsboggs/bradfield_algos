import unittest
from solutions import frog

class FrogTest(unittest.TestCase):
  def test_input1(self):
    self.assertEqual(frog.stone_jump(4, [10, 30, 40, 20]), 30)

  def test_input2(self):
    self.assertEqual(frog.stone_jump(2, [10, 10]), 0)

  def test_input3(self):
    self.assertEqual(frog.stone_jump(6, [30, 10, 60, 10, 60, 50]), 40)

if __name__ == "__main__":
  unittest.main()
