import unittest


def magic_index_distinct_bs(a, lower, upper):
    if lower == upper:
        return None
    middle = int((lower + upper) / 2)
    print(a, middle)
    if a[middle] == middle:
        return a[middle]
    elif a[middle] < middle:
        return magic_index_distinct_bs(a, middle+1, upper)
    else:
        return magic_index_distinct_bs(a, lower, middle)


def magic_index_distinct(a):
    if len(a) == 0 or a[0] > 0 or a[-1] < len(a) - 1:
        return None
    return magic_index_distinct_bs(a, 0, len(a))


def magic_index(a):
    for i, n in enumerate(a):
        if i == n:
            return n

    return None


class Test(unittest.TestCase):
    def test_magic_index_distinct(self):
        self.assertEqual(magic_index_distinct([3, 4, 5]), None)
        self.assertEqual(magic_index_distinct([-2, -1, 0, 2]), None)
        self.assertEqual(magic_index_distinct([-20, 0, 1, 2, 3, 4, 5, 6, 20]), None)
        self.assertEqual(magic_index_distinct([-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index_distinct([-20, 1, 2, 3, 4, 5, 6, 20]), 4)

    def test_magic_index(self):
        self.assertEqual(magic_index([3, 4, 5]), None)
        self.assertEqual(magic_index([-2, -1, 0, 2]), None)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 6, 20]), None)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index([-20, 1, 2, 3, 4, 5, 6, 20]), 1)
        self.assertEqual(magic_index([-20, 5, 5, 5, 5, 5, 6, 20]), 5)


if __name__ == '__main__':
    unittest.main()