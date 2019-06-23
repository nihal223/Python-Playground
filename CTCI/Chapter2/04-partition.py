import unittest

class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string

    def append_to_tail(self, val):
        while self.next:
            self = self.next
        self.next = Node(val)


def partition(head, x):
    node = head
    before = Node(None)
    after = Node(None)
    while node:
        if node.data < x:
            before.append_to_tail(node.data)
        else:
            after.append_to_tail(node.data)
        node = node.next

    before = before.next
    after = after.next

    temp = before
    while temp.next:
        temp = temp.next

    temp.next = after

    return before


class Test(unittest.TestCase):
  def test_partition(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition(head1, 6)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = partition(head2, 7)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")

if __name__ == "__main__":
    unittest.main()