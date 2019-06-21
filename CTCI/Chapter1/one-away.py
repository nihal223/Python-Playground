import unittest

def one_away(s1,s2):
    if s1 == s2:
        return True

    if abs(len(s1) - len(s2)) >= 2:
        return False

    letters = [0 for _ in range(128)]

    for char in s1:
        letters[ord(char)] += 1
    for char in s2:
        letters[ord(char)] += 1

    zero_count = 0
    for n in letters:
        if n==0:
            zero_count += 1

    if len(s1) == len(s2):
        if zero_count < 128 - max(len(s1), len(s2)) - 1:
            return False
    else:
        if zero_count < 128 - max(len(s1), len(s2)):
            return False

    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    # s1 = 'pal'
    # s2 = 'palks'
    # res = one_away(s1,s2)
    # print(res)