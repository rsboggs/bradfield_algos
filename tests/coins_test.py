import unittest
from solutions import coins

class CoinsTest(unittest.TestCase):
  def test_can_solve_simple_case(self):
    input_coins = [1, 2, 5]
    self.assertEqual(coins.minimum_count(input_coins, 11), 3)

if __name__ == "__main__":
  unittest.main()
