import pdb

class Stack(object):
  def __init__(self):
      self._items = []

  def is_empty(self):
      return not bool(self._items)

  def push(self, item):
      self._items.append(item)

  def pop(self):
      return self._items.pop()

  def peek(self):
      return self._items[-1]

  def size(self):
      return len(self._items)

def reverse_with_stack(items):
  item_stack = Stack()
  for item in items:
    item_stack.push(item)

  reversed = []
  while not item_stack.is_empty():
    reversed.append(item_stack.pop())

  return reversed
