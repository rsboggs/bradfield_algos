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

class Queue(object):
  def __init__(self):
    self._adding_stack = Stack()
    self._removal_stack = Stack()

  def is_empty(self):
    return self.size() == 0

  def enqueue(self, item):
    self._adding_stack.push(item)

  def dequeue(self):
    if self._removal_stack.is_empty():
      while not self._adding_stack.is_empty():
        self._removal_stack.push(self._adding_stack.pop())
    return self._removal_stack.pop()

  def size(self):
    return self._adding_stack.size() + self._removal_stack.size()
