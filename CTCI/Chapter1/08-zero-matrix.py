def zero_matrix(m):
    for i in range(len(m)):
        if 0 in m[i]:
            m[i] = [0 for _ in range(len(m[i]))]

    return m

def zero_matrix_rotate(m):
    m_r = list(zip(*m[::-1]))
    for i in range(len(m_r)):
        if 0 in m_r[i]:
            m_r[i] = [0 for _ in range(len(m_r[i]))]

    m1 = list(zip(*m_r[::-1]))
    m2 = list(zip(*m1[::-1]))
    m3 = list(zip(*m2[::-1]))

    return m3

def final_matrix(m1,m2):
    final_m = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if m1[i][j] == 0 or m2[i][j] == 0:
                final_m[i][j] = 0
            else:
                final_m[i][j] = m1[i][j]

    return final_m


if __name__ == '__main__':
    matrix = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    matrix_copy = matrix.copy()
    print(matrix)
    res1 = zero_matrix(matrix)
    print(res1)
    res2 = zero_matrix_rotate(matrix_copy)
    print(res2)
    res3 = final_matrix(res1,res2)
    print(res3)
