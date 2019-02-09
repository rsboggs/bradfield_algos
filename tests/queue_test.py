import unittest
from solutions import queue

class QueueTest(unittest.TestCase):
  def test_queue_if_empty(self):
    stack_queue = queue.Queue()
    self.assertEqual(stack_queue.is_empty(), True)

    stack_queue.enqueue(123)
    self.assertEqual(stack_queue.is_empty(), False)

  def test_queue_size(self):
    stack_queue = queue.Queue()
    stack_queue.enqueue(1)
    stack_queue.enqueue(2)
    stack_queue.enqueue(3)
    self.assertEqual(stack_queue.size(), 3)
    stack_queue.dequeue()
    self.assertEqual(stack_queue.size(), 2)

  def test_enqueue_and_dequeue_order(self):
    stack_queue = queue.Queue()
    stack_queue.enqueue(1)
    stack_queue.enqueue(2)
    self.assertEqual(stack_queue.size(), 2)
    self.assertEqual(stack_queue.dequeue(), 1)
    self.assertEqual(stack_queue.size(), 1)
    stack_queue.enqueue(3)
    self.assertEqual(stack_queue.dequeue(), 2)

if __name__ == "__main__":
  unittest.main()
