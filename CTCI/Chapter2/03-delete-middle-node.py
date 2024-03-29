import unittest


class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def delete_middle(node):
    next = node.next
    node.data = next.data
    node.next = next.next



class Test(unittest.TestCase):
    def test_delete_middle(self):
        head = Node(1, Node(2, Node(3, Node(4))))
        delete_middle(head.next.next)
        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 2)
        self.assertEqual(head.next.next.data, 4)


if __name__ == '__main__':
    unittest.main()

