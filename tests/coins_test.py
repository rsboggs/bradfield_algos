import unittest
from solutions import coins

class CoinsTest(unittest.TestCase):
  def test_can_solve_one_coin(self):
    input_coins = [1, 2, 5]
    self.assertEqual(coins.minimum_count2(input_coins, 2), 1)

  def test_can_solve_two_coin(self):
    input_coins = [1, 2, 5]
    self.assertEqual(coins.minimum_count2(input_coins, 3), 2)

  def test_can_solve_case(self):
    input_coins = [1, 2, 5]
    self.assertEqual(coins.minimum_count2(input_coins, 7), 2)

  def test_can_solve_case2(self):
    input_coins = [1, 2, 5]
    self.assertEqual(coins.minimum_count2(input_coins, 11), 3)

  def test_can_solve_case3(self):
    input_coins = [2,5,10,1]
    self.assertEqual(coins.minimum_count2(input_coins, 27), 4)

  def test_can_solve_case4(self):
    input_coins = [186,419,83,408]
    self.assertEqual(coins.minimum_count2(input_coins, 6249), 20)

  def test_will_return_negative_one_if_not_possible(self):
    input_coins = [2, 5]
    self.assertEqual(coins.minimum_count2(input_coins, 3), -1)

  def test_will_return_negative_one_if_not_possible2(self):
    input_coins = [2]
    self.assertEqual(coins.minimum_count2(input_coins, 3), -1)

if __name__ == "__main__":
  unittest.main()
