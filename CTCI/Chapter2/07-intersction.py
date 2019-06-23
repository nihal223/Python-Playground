import unittest


class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string


def intersection(head1, head2):
    node1 = head1
    node2 = head2
    nodes = {}
    while node1:
        nodes[node1] = True
        node1 = node1.next
    while node2:
        if node2 in nodes:
            return node2
        nodes[node2] = True
        node2 = node2.next

    return None


class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection(head3, head4), node)



if __name__ == '__main__':
    unittest.main()

