import unittest
from collections import defaultdict


def build_order():
    return


class Test(unittest.TestCase):
    def test_build_order(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]


if __name__=='__main__':
    unittest.main()