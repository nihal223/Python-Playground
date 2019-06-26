import unittest


class Stack():
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if len(self.array) == 0:
            return None
        return self.array.pop()


class QueueViaStacks():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def add(self, item):
        self.stack1.push(item)

    def remove(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

class Test(unittest.TestCase):
  def test_queue_via_stacks(self):
    queue = QueueViaStacks()
    queue.add(11)
    queue.add(22)
    queue.add(33)
    self.assertEqual(queue.remove(), 11)
    queue.add(44)
    queue.add(55)
    queue.add(66)
    self.assertEqual(queue.remove(), 22)
    self.assertEqual(queue.remove(), 33)
    self.assertEqual(queue.remove(), 44)
    self.assertEqual(queue.remove(), 55)
    queue.add(77)
    self.assertEqual(queue.remove(), 66)
    self.assertEqual(queue.remove(), 77)
    self.assertEqual(queue.remove(), None)


if __name__ == '__main__':
    unittest.main()