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


def bst_seqs(root):
    return bst_seq_partial([], [root])


def bst_seq_partial(partial, subtrees):
    if not(len(subtrees)):
        return [partial]
    sequences = []
    for index, subtree in enumerate(subtrees):
        next_partial = partial + [subtree.data]
        next_subtrees = subtrees[:index] + subtrees[index + 1:]
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)
        sequences += bst_seq_partial(next_partial, next_subtrees)
    return sequences



class Test(unittest.TestCase):
    def test_bst_seqs(self):
        root = Node(7)
        root.left = Node(4)
        root.right = Node(9)
        root.left.right = Node(5)

        printTree(root)

        self.assertEqual(bst_seqs(root), [
          [7, 4, 9, 5],
          [7, 4, 5, 9],
          [7, 9, 4, 5]])


if __name__=='__main__':
    unittest.main()