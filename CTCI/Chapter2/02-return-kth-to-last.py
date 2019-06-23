import unittest


class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

def ll_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def kth_to_last(head, k):
    node = head
    if k==0 or k > ll_length(node):
        return None

    psuedo_k = ll_length(node) - k
    for i in range(psuedo_k):
        node = node.next

    return node


class Test(unittest.TestCase):
    def test_kth_to_last(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
        self.assertEqual(None, kth_to_last(head, 0))
        self.assertEqual(7, kth_to_last(head, 1).data)
        self.assertEqual(4, kth_to_last(head, 4).data)
        self.assertEqual(2, kth_to_last(head, 6).data)
        self.assertEqual(1, kth_to_last(head, 7).data)
        self.assertEqual(None, kth_to_last(head, 8))


if __name__ == '__main__':
    unittest.main()