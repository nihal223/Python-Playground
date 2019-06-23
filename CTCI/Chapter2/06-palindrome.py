import unittest


class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

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


def is_palindrome(head):
    node = head
    if node.next == None:
        return True

    node_rev = node.reverse()

    count1 = 0
    count2 = 0
    while node:
        count1 += 1
        if node.data == node_rev.data:
            count2+=1
        node = node.next

    if count1 == count2:
        return True
    return False


class Test(unittest.TestCase):
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome(list4))


if __name__ == '__main__':
    unittest.main()

