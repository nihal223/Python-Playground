import unittest
from collections import deque


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def printTree(root):
    print('\n')
    buf = deque()
    output = []
    if not root:
        print('$')
    else:
        buf.append(root)
        count, nextCount = 1, 0
        while count:
            node = buf.popleft()
            if node:
                output.append(node.data)
                count -= 1
                for n in (node.left, node.right):
                    if n:
                        buf.append(n)
                        nextCount += 1
                    else:
                        buf.append(None)
            else:
                output.append('$')
            if not count:
                print(output)
                output = []
                count, nextCount = nextCount, 0
        # print the remaining all empty leaf node part
        output.extend(['$']*len(buf))
        print(output)


def first_common_ancestor(root, node1, node2):
    if root is None:
        return None

    if root.data == node1 or root.data == node2:
        return root

    left_fca = first_common_ancestor(root.left, node1, node2)
    right_fca = first_common_ancestor(root.right, node1, node2)


    if left_fca and right_fca:
        return root

    return left_fca if left_fca else right_fca


class Test(unittest.TestCase):
    def test_validate_BST(self):
        root = Node(7)
        root.left = Node(5)
        root.right = Node(10)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.right = Node(11)

        printTree(root)

        self.assertEqual(first_common_ancestor(root, 5, 10).data, 7)
        self.assertEqual(first_common_ancestor(root, 5, 11).data, 7)
        self.assertEqual(first_common_ancestor(root, 4, 6).data, 5)
        self.assertEqual(first_common_ancestor(root, 5, 7).data, 7)


if __name__=='__main__':
    unittest.main()