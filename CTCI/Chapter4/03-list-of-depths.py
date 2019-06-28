import unittest


class NodeT():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class NodeLL():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print(self):
        res = ''
        node = self
        while node:
            res += str(node.data)
            node = node.next
        print(res)

def list_of_depths(root):
    res = []

    q = []

    q.append(root)
    res.append([NodeLL(root.data)])

    while q:
        x = q.pop(0)
        sub_ll = NodeLL(None)
        temp = sub_ll

        if x.left:
            q.append(x.left)
            temp.next = NodeLL(x.left.data)
            temp = temp.next

        if x.right:
            q.append(x.right)
            temp.next = NodeLL(x.right.data)
            temp = temp.next

        sub_ll = sub_ll.next
        res.append([sub_ll])
    return res



class Test(unittest.TestCase):
    def test_list_of_depths(self):
        root = NodeT(3)
        root.left = NodeT(2)
        root.right = NodeT(5)
        root.left.left = NodeT(1)
        root.right.left = NodeT(4)

        list_of_ll = list_of_depths(root)
        for i in list_of_ll:
            print(i)
        self.assertEqual(len(list_of_ll), 3)

        return

if __name__ == '__main__':
    unittest.main()