import unittest

def count_steps_(n, res):
    if n == 1:
        res[n] = 1
    elif n == 2:
        res[n] = 2
    elif n == 3:
        res[n] = 4
    else:
        if n not in res:
            res[n] =  count_steps_(n-1, res) + count_steps_(n-2, res) + count_steps_(n-3, res)

    return res[n]

def count_steps(n):
    return count_steps_(n, {})



class Test(unittest.TestCase):
    def test_count_steps(self):
        self.assertEqual(count_steps(3), 4)
        self.assertEqual(count_steps(7), 44)


if __name__ == '__main__':
    unittest.main()