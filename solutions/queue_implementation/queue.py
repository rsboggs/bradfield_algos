class PythonListQueue(object):
  """
  A queue based on the built in Python list type.
  """
  def __init__(self):
    self._items = []

  def enqueue(self, item):
    self._items.append(item)

  def dequeue(self):
    return self._items.pop(0)

  def size(self):
    return len(self._items)

  def is_empty(self):
    return len(self._items) == 0


class LinkedListNode(object):
  """
  A doubly linked list node, support for the LinkedListQueue. You should not need
  to change this code, but you will want to use it in the LinkedListQueue
  """
  def __init__(self, value, prevNode, nextNode):
    self.value = value
    self.prev = prevNode
    self.next = nextNode


class LinkedListQueue(object):
  """
  Finish the functions below to create a queue based on a linked list. Because
  a queue must either:

    * enqueue to the head and dequeue from the tail; or
    * enqueue to the tail and dequeue from the head.

  You should use a doubly linked list to ensure O(1) time enqueue and dequeue.
  """
  def __init__(self):
    self._head = None
    self._tail = None

  # O(1)
  def enqueue(self, item):
    if self._head == None:
      self._head = LinkedListNode(item, None, None)
      self._tail = self._head
    else:
      former_head = self._head
      self._head = LinkedListNode(item, None, former_head)
      former_head.prev = self._head

  # O(1)
  def dequeue(self):
    tail_value = self._tail.value
    self._tail = self._tail.prev
    if self._tail == None or self._tail.prev == None:
      self._head = self._tail

    if self._tail != None:
      self._tail.next = None
    return tail_value

  # O(n)
  def size(self):
    current_node = self._head
    counter = 0
    while current_node:
      counter += 1
      current_node = current_node.next
    return counter

  # O(1)
  def is_empty(self):
    return self._head == None


class RingBufferQueue(object):
  """
  Finish the functions below such that this queue is backed by a Ring Buffer.
  Recall that a ring buffer uses an array and two pointers to keep track of
  where to read, and where to write.

  Be careful! If the read pointer were to overtake the write pointer, it
  would return incorrect data! If the write pointer were to overtake the read
  pointer, it would overwrite data that hasn't been read yet!

  In many contexts, you would avoid this issue by stalling when one pointer
  would overwrite the other. Since doing so only makes sense in a multithreaded
  environment, you may prefer to just resize the underlying ring buffer at
  these times, instead.
  """
  def __init__(self):
    pass

  def enqueue(self, item):
    pass

  def dequeue(self):
    pass

  def size(self):
    pass

  def is_empty(self):
    pass


QUEUE_CLASSES = (
  PythonListQueue,
  LinkedListQueue,
  RingBufferQueue,
)

