import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_helper(root):
    # a None tree is balanced
    if root is None:
        return 0
    left_height = is_balanced_helper(root.left)
    # if the left subtree is not balanced, then:
    # this tree is also not balanced
    if left_height == -1:
        return -1
    # if the right subtree is not balanced, then:
    # this tree is also not balanced
    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1
    # if the diffrence in heights is greater than 1, then:
    # this tree is not balanced
    if abs(left_height - right_height) > 1:
        return -1
    # this tree is balanced, return its height
    return max(left_height, right_height) + 1


def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left), height(root.right))


def check_balanced(root):
    if root is None:
        return True
    print(root.data)
    return check_balanced(root.left) and check_balanced(root.right) and abs(height(root.left) - height(root.right)) <= 1


class Test(unittest.TestCase):
    def test_check_balanced(self):
        root = Node(3)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.right.left = Node(4)
        self.assertEqual(check_balanced(root), True)

        root = Node(3)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        self.assertEqual(check_balanced(root), True)

        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        self.assertEqual(check_balanced(root), False)


if __name__=='__main__':
    unittest.main()