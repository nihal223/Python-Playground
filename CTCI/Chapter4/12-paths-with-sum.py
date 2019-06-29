import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def paths_with_sum(root, k):
    def traverse(root, val):
        if not root: return 0
        res = (val == root.data)
        print(root.data, res)
        res += traverse(root.left, val - root.data)
        res += traverse(root.right, val - root.data)
        print("trav done")
        return res

    if not root: return 0
    ans = traverse(root, k)
    ans += paths_with_sum(root.left, k)
    ans += paths_with_sum(root.right, k)
    return ans


class Test(unittest.TestCase):
    def test_paths_with_sum(self):
        root = Node(2)
        root.left = Node(1)
        root.right = Node(6)
        root.left.left = Node(6)
        root.left.right = Node(5)
        root.right.left = Node(1)
        root.right.right = Node(2)

        self.assertEqual(paths_with_sum(root, 8), 3,)


if __name__ == '__main__':
    unittest.main()