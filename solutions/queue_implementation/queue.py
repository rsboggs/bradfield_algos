class PythonListQueue(object):
  """
  A queue based on the built in Python list type.
  """
  def __init__(self):
    self._items = []

  # O(1)
  def enqueue(self, item):
    self._items.append(item)

  # O(n)
  def dequeue(self):
    return self._items.pop(0)

  # O(1)
  def size(self):
    return len(self._items)

  # O(1)
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
    self._node_count = 0

  # O(1)
  def enqueue(self, item):
    if self._head == None:
      self._head = LinkedListNode(item, None, None)
      self._tail = self._head
    else:
      former_head = self._head
      self._head = LinkedListNode(item, None, former_head)
      former_head.prev = self._head
    self._node_count += 1

  # O(1)
  def dequeue(self):
    tail_value = self._tail.value
    self._tail = self._tail.prev
    if self._tail == None or self._tail.prev == None:
      self._head = self._tail

    if self._tail != None:
      self._tail.next = None
    self._node_count -= 1
    return tail_value

  # O(1)
  def size(self):
    return self._node_count

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
    self._buffer_size = 2
    self._buffer = [None] * self._buffer_size
    self._start_index = 0
    self._end_index = 0

  # O(1) ("amortized" because of resize)
  def enqueue(self, item):
    if self._next_index(self._end_index) == self._start_index:
      self._resize()
    self._buffer[self._end_index] = item
    self._end_index = self._next_index(self._end_index)

  # O(1)
  def dequeue(self):
    value = self._buffer[self._start_index]
    self._start_index = self._next_index(self._start_index)
    return value

  # O(1)
  def size(self):
    if self._end_index > self._start_index:
      return self._end_index - self._start_index
    else:
      return self._end_index + (self._buffer_size - self._start_index)

  # O(1)
  def is_empty(self):
    return self._start_index == self._end_index

  # Helpers
  def _next_index(self, index):
    return (index + 1) % self._buffer_size

  def _resize(self):
    current_buffer_size = self._buffer_size
    current_buffer = self._buffer
    self._buffer_size = current_buffer_size * 2
    self._buffer = [None] * self._buffer_size
    new_index = 0
    if self._end_index > self._start_index:
      for index in range(self._start_index, self._end_index):
        self._buffer[new_index] = current_buffer[index]
        new_index += 1
    else:
      for index in range(self._start_index, current_buffer_size):
        self._buffer[new_index] = current_buffer[index]
        new_index += 1
      for index in range(0, self._end_index):
        self._buffer[new_index] = current_buffer[index]
        new_index += 1
    self._start_index = 0
    self._end_index = current_buffer_size - 1




QUEUE_CLASSES = (
  PythonListQueue,
  LinkedListQueue,
  RingBufferQueue,
)

