class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

  def min_depth(self):
    # Needed for leetcode edge case
    if not self:
      return 0

    nodes = [(self, 1)]
    while len(nodes) > 0:
      # Would use linked list if want to boost performance of this operation
      current_node, current_count = nodes.pop(0)
      if current_node.left == None and current_node.right == None:
        return current_count

      if current_node.left != None:
        nodes.append((current_node.left, current_count + 1))
      if current_node.right != None:
        nodes.append((current_node.right, current_count + 1))
