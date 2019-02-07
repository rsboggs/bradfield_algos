import unittest
from solutions import spiral

class SpiralTest(unittest.TestCase):
  def test_with_input2(self):
    expected = [
      [1, 2],
      [4, 3],
    ]
    self.assertEqual(spiral.create_spiral_matrix(2), expected)

  def test_with_input3(self):
    expected = [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5],
    ]
    self.assertEqual(spiral.create_spiral_matrix(3), expected)

  def test_with_input4(self):
    expected = [
      [1, 2, 3, 4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10, 9, 8, 7],
    ]
    self.assertEqual(spiral.create_spiral_matrix(4), expected)

if __name__ == '__main__':
  unittest.main()
