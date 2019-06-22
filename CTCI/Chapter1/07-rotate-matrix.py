def rotate_matrix(matrix):
    # Reverse the order and makes new lists from the corresponding 1st, 2nd ... nth element from the sublists
    return list(zip(*matrix[::-1]))


if __name__ == '__main__':
    matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    res = rotate_matrix(matrix)
    print(res)