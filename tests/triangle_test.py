import unittest
from solutions import triangle

class TriangleTest(unittest.TestCase):
  def test_sample_case(self):
    input = [
      [2],
      [3,4],
      [6,5,7],
      [4,1,8,3]
    ]
    self.assertEqual(triangle.minimum_total(input), 11)
