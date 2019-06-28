import unittest


INT_MAX = 4294967296
INT_MIN = -4294967296


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validate_BST(root):
    return validate_BST_util(root, INT_MIN, INT_MAX)


def validate_BST_util(root, min, max):
    if not root:
        return True

    if root.data < min or root.data > max:
        return False

    return (validate_BST_util(root.left, min, root.data - 1) and validate_BST_util(root.right, root.data + 1, max))


class Test(unittest.TestCase):
    def test_validate_BST(self):
        root = Node(7)
        root.left = Node(5)
        root.right = Node(10)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.right = Node(11)
        self.assertEqual(validate_BST(root), True)

        root = Node(7)
        root.left = Node(5)
        root.right = Node(10)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.right = Node(11)
        root.right.left = Node(1)
        self.assertEqual(validate_BST(root), False)


if __name__=='__main__':
    unittest.main()