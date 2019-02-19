import unittest
from solutions import dijkstra

class DijkstraTest(unittest.TestCase):
  def test_two_points(self):
      times = [[2,1,3]]
      N = 1
      K = 2
      expected = 3
      self.assertEqual(
        dijkstra.network_delay_time(times, N, K),
        expected
      )

  def test_two_points_return_negative_one_if_not_found(self):
    times = [[1,2,1]]
    N = 2
    K = 2
    expected = -1
    self.assertEqual(
      dijkstra.network_delay_time(times, N, K),
      expected
    )

  def test_simple_several_points(self):
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    expected = 2
    self.assertEqual(
      dijkstra.network_delay_time(times, N, K),
      expected
    )

  def test_another_case(self):
    times = [[1,2,1],[2,3,2],[1,3,2]]
    N = 3
    K = 1
    expected = 2
    self.assertEqual(
      dijkstra.network_delay_time(times, N, K),
      expected
    )

if __name__ == "__main__":
  unittest.main()
