import unittest
from solutions import pangram

class PanagramTest(unittest.TestCase):
  def test_invalid_length_text(self):
    self.assertEqual(pangram.is_pangram_1("abc"), False)
    self.assertEqual(pangram.is_pangram_2("abc"), False)
    self.assertEqual(pangram.is_pangram_3("abc"), False)

  def test_invalid_missing_chars_text(self):
    self.assertEqual(pangram.is_pangram_1("abcdefghijklmnopqrstuvwxyyyy"), False)
    self.assertEqual(pangram.is_pangram_2("abcdefghijklmnopqrstuvwxyyyy"), False)
    self.assertEqual(pangram.is_pangram_3("abcdefghijklmnopqrstuvwxyyyy"), False)

  def test_valid_text(self):
    self.assertEqual(pangram.is_pangram_1("abcdefghijklmnopqrstuvwxzyaaaaazzzzeee"), True)
    self.assertEqual(pangram.is_pangram_2("abcdefghijklmnopqrstuvwxzyaaaaazzzzeee"), True)
    self.assertEqual(pangram.is_pangram_3("abcdefghijklmnopqrstuvwxzyaaaaazzzzeee"), True)

  def test_valid_with_spaces_text(self):
    self.assertEqual(pangram.is_pangram_1("the quick brown fox jumps over the lazy dog"), True)
    self.assertEqual(pangram.is_pangram_2("the quick brown fox jumps over the lazy dog"), True)
    self.assertEqual(pangram.is_pangram_3("the quick brown fox jumps over the lazy dog"), True)

if __name__ == '__main__':
  unittest.main()
