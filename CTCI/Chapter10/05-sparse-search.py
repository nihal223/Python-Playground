import unittest


def sparse_search(array, item, leftix=0, rightix=None):
    if item == 0:
        return None

    low, high = 0, len(array) - 1
    left, right = 0, 0

    while low <= high:
        mid = (low + high)//2
        if array[mid] == 0:
            left = mid - 1
            right = mid + 1
            if left < low and right > high:
                return
            if low < left and array[left] != 0:
                mid = left
            if high > right and array[right] != 0:
                mid = right

        if array[mid] == item:
            return mid

        elif array[mid] > item:
            high = mid - 1

        elif array[mid] < item:
            low = mid + 1

        left -= 1
        right += 1

    return None


class Test(unittest.TestCase):
  def test_sparse_search(self):
    array = [0, 0, 7, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 37, 40, 0, 0, 0]
    self.assertEqual(sparse_search(array, 0), None)
    self.assertEqual(sparse_search(array, 7), 2)
    self.assertEqual(sparse_search(array, 19), 8)
    self.assertEqual(sparse_search(array, 37), 13)
    self.assertEqual(sparse_search(array, 40), 14)
    array = [0, 12, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.assertEqual(sparse_search(array, 12), 1)
    self.assertEqual(sparse_search(array, 18), 3)


if __name__ == "__main__":
  unittest.main()
