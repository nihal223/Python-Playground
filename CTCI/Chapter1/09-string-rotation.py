import unittest

def is_substring(s1,s2):
    if s2 in s1:
        return True
    return False

def is_rotation(s1,s2):
    print(s1,s2)
    if len(s1) != len(s2):
        return False
    return is_substring(s1+s1,s2)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
