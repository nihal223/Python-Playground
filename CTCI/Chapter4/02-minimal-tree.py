import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimal_tree(a):
    if len(a) == 0:
        return

    if len(a) == 1:
        return Node(a[0])

    mid = int(len(a)/2)
    root = Node(a[mid])
    root.left = minimal_tree(a[:mid])
    root.right = minimal_tree(a[mid+1:])

    return root


class Test(unittest.TestCase):
    def test_minimal_tree(self):
        a = [1,2,3,4,5]
        self.assertEqual(minimal_tree(a).data, 3)
        self.assertEqual(minimal_tree(a).left.data, 2)
        self.assertEqual(minimal_tree(a).left.left.data, 1)
        self.assertEqual(minimal_tree(a).right.data, 5)
        self.assertEqual(minimal_tree(a).right.left.data, 4)


if __name__ == '__main__':
    unittest.main()