import unittest


class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string

    def reverse(self):
        prev = Node(None)
        prev = prev.next
        head = self
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        return head


def sum_lists(num1, num2):
    node1 = num1
    node2 = num2
    res =  Node(0)
    temp = res
    carry = Node(0)

    while node1 or node2:
        value = 0
        if node1:
            value += node1.data
            node1 = node1.next
        if node2:
            value += node2.data
            node2 = node2.next
        temp.next = Node( (value + carry.data)%10 )
        carry.next = Node( int(value/10) )

        carry, temp = carry.next, temp.next

    res = res.next
    return res


def sum_lists_forward(num1, num2):
    node1 = num1
    node2 = num2
    node1 = node1.reverse()
    node2 = node2.reverse()

    res =  Node(0)
    temp = res
    carry = Node(0)

    while node1 or node2:
        value = 0
        if node1:
            value += node1.data
            node1 = node1.next
        if node2:
            value += node2.data
            node2 = node2.next
        temp.next = Node( (value + carry.data)%10 )
        carry.next = Node( int(value/10) )

        carry, temp = carry.next, temp.next

    res = res.next
    return res



class Test(unittest.TestCase):
    def test_sum_lists(self):
        num1 = Node(3, Node(2, Node(1)))
        num2 = Node(5, Node(9, Node(4)))
        self.assertEqual(str(sum_lists_forward(num1, num2)), "5,1,9")
        num1 = Node(9, Node(2, Node(3, Node(4, Node(1)))))
        num2 = Node(4, Node(9, Node(8)))
        self.assertEqual(str(sum_lists(num1, num2)), "3,2,2,5,1")


if __name__ == '__main__':
    unittest.main()

