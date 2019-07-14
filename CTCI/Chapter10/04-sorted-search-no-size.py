import unittest


class Listy(object):
    def __init__(self, array):
        self.array = array

    def __getitem__(self, ix):
        if ix < len(self.array):
            return self.array[ix]
        else:
            return -1

def binary_search(arr, l ,r, x):
    if r >= l:
        mid = (l+r)//2
        if x == arr[mid]:
            return mid
        if x < arr[mid]:
            return binary_search(arr, l, mid-1, x)
        return binary_search(arr, mid+1, r, x)
    return None


def search_listy(listy, item):
    print("advadbadbda")
    l, h, val = 0, 1, listy[0]
    while val < item:
        l = h
        h = 2*h
        val = listy[h]

    return binary_search(listy, l, h, item)


class Test(unittest.TestCase):
    def test_search_listy(self):
        listy = Listy([-22, -11, 11, 22, 33, 44, 55, 66, 77, 88, 99])
        self.assertEqual(search_listy(listy, 25), None)
        self.assertEqual(search_listy(listy, -22), 0)
        self.assertEqual(search_listy(listy, 22), 3)
        self.assertEqual(search_listy(listy, 66), 7)
        self.assertEqual(search_listy(listy, 77), 8)
        self.assertEqual(search_listy(listy, 99), 10)
        # self.assertEqual(search_listy(listy, 100), None)


if __name__ == "__main__":
    unittest.main()