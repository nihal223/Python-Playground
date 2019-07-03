import unittest


def path_in_grid(grid):
    if len(grid) == 0:
        return []
    search = []
    for r, row in enumerate(grid):
        search.append([])
        for c, blocked in enumerate(row):
            if r == 0 and c == 0:
                search[r].append("start")
            elif blocked:
                search[r].append(None)
            elif r > 0 and search[r - 1][c]:
                search[r].append("down")
            elif c > 0 and search[r][c - 1]:
                search[r].append("right")
            else:
                search[r].append(None)

    path = ["end"]
    r, c = len(grid) - 1, len(grid[0]) - 1
    if not search[r][c]:
        return None

    while c > 0 or r > 0:
        path.append(search[r][c])
        if search[r][c] == "down":
            r -= 1
        else:
            c -= 1
    path.append("start")
    path.reverse()
    return path


class Test(unittest.TestCase):
    def test_path(self):
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(path_in_grid(grid), ["start", "right", "right",
                                                   "right", "down", "down", "right", "right", "right", "down", "end"])
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(path_in_grid(grid), None)


if __name__ == '__main__':
    unittest.main()