import unittest
from solutions import graph

class GraphTest(unittest.TestCase):
  def test_finds_minimum_depth_for_simple_tree(self):
    tree = graph.TreeNode(4)
    self.assertEqual(tree.min_depth(), 1)

  def test_finds_minimum_depth_for_even_two_depth_tree(self):
    tree = graph.TreeNode(4)
    tree.left = graph.TreeNode(3)
    tree.right = graph.TreeNode(5)
    self.assertEqual(tree.min_depth(), 2)

  def test_finds_minimum_depth_for_uneven_left_two_depth_tree(self):
    tree = graph.TreeNode(4)
    tree.left = graph.TreeNode(3)
    tree.right = graph.TreeNode(5)
    tree.right.right = graph.TreeNode(6)
    self.assertEqual(tree.min_depth(), 2)

  def test_finds_minimum_depth_for_uneven_right_two_depth_tree(self):
    tree = graph.TreeNode(4)
    tree.left = graph.TreeNode(3)
    tree.right = graph.TreeNode(5)
    tree.right.left = graph.TreeNode(6)
    self.assertEqual(tree.min_depth(), 2)

  def test_finds_minimum_depth_for_one_sided_two_depth_tree(self):
    tree = graph.TreeNode(4)
    tree.left = graph.TreeNode(3)
    self.assertEqual(tree.min_depth(), 2)

if __name__ == "__main__":
  unittest.main()
