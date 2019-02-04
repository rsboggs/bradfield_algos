import unittest
from solutions import pangram

class PanagramTest(unittest.TestCase):
  def test_invalid_length_text(self):
    self._evaluate_each_method("abc", False)

  def test_invalid_missing_chars_text(self):
    self._evaluate_each_method("abcdefghijklmnopqrstuvwxyyyy", False)

  def test_valid_text(self):
    self._evaluate_each_method("abcdefghijklmnopqrstuvwxzyaaaaazzzzeee", True)

  def test_valid_with_spaces_text(self):
    self._evaluate_each_method("the quick brown fox jumps over the lazy dog", True)

  def _evaluate_each_method(self, text, expected_value):
    for index in range(3):
      method_name = f'is_pangram_{index + 1}'
      self.assertEqual(getattr(pangram, method_name)(text), expected_value)

if __name__ == '__main__':
  unittest.main()
