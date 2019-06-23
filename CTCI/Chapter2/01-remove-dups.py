import unittest


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


def remove_dups(head):
    node = head
    if node:
        values = {node.data: True}
        while node.next:
            if node.next.data in values:
                node.next = node.next.next
            else:
                values[node.next.data] = True
                node = node.next

def remove_dups_followup(head):
    node = head
    if node:
        while node:
            runner = node
            while runner.next:
                if runner.next.data == node.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            node = node.next


class Test(unittest.TestCase):
    def test_remove_dups(self):
        head = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
        remove_dups_followup(head)
        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 3)
        self.assertEqual(head.next.next.data, 5)
        self.assertEqual(head.next.next.next, None)


if __name__ == '__main__':
    unittest.main()
