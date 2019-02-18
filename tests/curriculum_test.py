import unittest
from solutions import curriculum

class CurriculumTest(unittest.TestCase):
  def test_passing_single_class(self):
    classes = [
      {
        "title": "Algos",
        "prereqs": [],
      },
    ]
    self.assertTrue(curriculum.is_possible_curriculum(classes))

  def test_passing_2_classes_no_prereqs(self):
    classes = [
      {
        "title": "Algos",
        "prereqs": [],
      },
      {
        "title": "Computer Arch",
        "prereqs": [],
      },
    ]
    self.assertTrue(curriculum.is_possible_curriculum(classes))

  def test_passing_2_classes_one_with_other_as_prereq(self):
    classes = [
      {
        "title": "Algos",
        "prereqs": [],
      },
      {
        "title": "Computer Arch",
        "prereqs": ["Algos"],
      },
    ]
    self.assertTrue(curriculum.is_possible_curriculum(classes))

  def test_fails_2_classes_each_prereqs(self):
    classes = [
      {
        "title": "Algos",
        "prereqs": ["Computer Arch"],
      },
      {
        "title": "Computer Arch",
        "prereqs": ["Algos"],
      },
    ]
    self.assertFalse(curriculum.is_possible_curriculum(classes))

  def test_fails_3_classes_each_prereqs(self):
    classes = [
      {
        "title": "Algos",
        "prereqs": ["Languages"],
      },
      {
        "title": "Computer Arch",
        "prereqs": ["Algos"],
      },
      {
        "title": "Languages",
        "prereqs": ["Computer Arch"],
      },
    ]
    self.assertFalse(curriculum.is_possible_curriculum(classes))

  def test_passing_3_classes_ok_prereqs(self):
    classes = [
      {
        "title": "Computer Arch",
        "prereqs": ["Algos"],
      },
      {
        "title": "Languages",
        "prereqs": ["Computer Arch"],
      },
      {
        "title": "Algos",
        "prereqs": [],
      },
    ]
    self.assertTrue(curriculum.is_possible_curriculum(classes))

if __name__ == "__main__":
  unittest.main()
