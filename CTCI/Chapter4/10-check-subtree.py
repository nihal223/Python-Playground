import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order_subtree(r, res):
    if not r:
       return None
    res.append(r.data)
    pre_order_subtree(r.left, res)
    pre_order_subtree(r.right, res)

    return res

def check_subtree(root1, root2):
    if not root1:
        return None
    x = root1
    if pre_order_subtree(x, []) == pre_order_subtree(root2, []):
        return True

    if check_subtree(root1.left, root2) or check_subtree(root1.right, root2):
        return True
    else:
        return False




class Test(unittest.TestCase):
    def test_check_subtree(self):
        root1 = Node(10)
        root1.left = Node(2)
        root1.right = Node(3)
        root1.left.left = Node(1)
        root1.left.right = Node(6)

        root2 = Node(2)
        root2.left = Node(1)
        root2.right = Node(6)

        self.assertEqual(check_subtree(root1, root2), True)


if __name__ == '__main__':
    unittest.main()