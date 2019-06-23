import unittest


class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string

def detect_loop_floyd(head):
    slow_p = head
    fast_p = head
    while (slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return slow_p.data
    return None


def detect_loop(head):
    nodes = {}
    node = head
    while node:
        if node in nodes:
            return node
        nodes[node] = True
        node = node.next
    return None


class Test(unittest.TestCase):
  def test_detect_loop(self):
      head1 = Node(100, Node(200, Node(300)))
      self.assertEqual(detect_loop(head1), None)
      node1 = Node(600)
      node2 = Node(700, Node(800, Node(900, node1)))
      node1.next = node2
      head2 = Node(500, node1)
      self.assertEqual(detect_loop(head2), node1)



if __name__ == '__main__':
    unittest.main()

