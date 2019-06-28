import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def successor(root, node):
    if root == node:
        return root.right.data

    if node.data > root.data:
        return successor(root.right, node)
    else:
        return successor(root.left, node)


class Test(unittest.TestCase):
    def test_validate_BST(self):
        root = Node(7)
        root.left = Node(5)
        root.right = Node(10)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.right = Node(11)
        self.assertEqual(successor(root, root), 10)
        self.assertEqual(successor(root, root.left), 6)
        self.assertEqual(successor(root, root.right), 11)


if __name__=='__main__':
    unittest.main()