import unittest


def permutations(s):
    return permutations_(s, "")


def permutations_(letters_left, partial):
    print('\n', letters_left, partial)
    if len(letters_left)==0:
        return [partial]
    perm = []
    for i, char in enumerate(letters_left):
        next_letters_left = letters_left[:i] + letters_left[(i+1):]
        perm += permutations_(next_letters_left, partial+char)
    return perm


class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutations("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])


if __name__ == "__main__":
  unittest.main()