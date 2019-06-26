import unittest


class Stack():
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if len(self.array) == 0:
            return None
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def is_empty(self):
        if len(self) == 0:
            return True
        return False


    def sort_stack(self):
        temp = Stack()
        if temp.is_empty():
            temp.push(self.array.pop())

        while self.array:
            if self.peek() > temp.peek():
                item_temp = temp.pop()
                item_a = self.pop()
                temp.push(item_a)
                self.push(item_temp)
            else:
                temp.push(self.pop())

        return temp.array


class Test(unittest.TestCase):
    def test_sort_stack(self):
        a = Stack()
        a.push(2)
        a.push(1)
        a.push(4)
        a.push(3)
        self.assertEqual(a.array, [2,1,4,3])
        # smallest on the top
        self.assertEqual(a.sort_stack(), [4,3,2,1])


if __name__ == '__main__':
    unittest.main()