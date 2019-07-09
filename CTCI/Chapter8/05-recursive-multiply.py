import unittest


def multiply(a, b):
    c = 0
    while (b != 0):
        if (b & 1 != 0):
            c += a
        b = b >> 1
        a = a << 1
    return c


class Test(unittest.TestCase):
  def test_multiply(self):
    self.assertEqual(multiply(2, 2), 4)
    self.assertEqual(multiply(1, 125), 125)
    self.assertEqual(multiply(7, 11), 77)
    self.assertEqual(multiply(10000000010, 21), 210000000210)

if __name__ == "__main__":
  unittest.main()
