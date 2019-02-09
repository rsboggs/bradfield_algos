import unittest
from solutions import reverse

class ReverseTest(unittest.TestCase):
  def test_list_is_reversed(self):
    self.assertEqual(reverse.reverse_with_stack([1, 2, 3]), [3, 2, 1])

if __name__ == "__main__":
  unittest.main()
