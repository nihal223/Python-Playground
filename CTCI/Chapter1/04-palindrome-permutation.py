def pp(s):
    ss = s.replace(' ', '').lower()
    ss_sorted = sorted(ss)
    n = len(ss_sorted)

    if n % 2 == 0:
        for i in range(0, n-1, 2):
            if ss_sorted[i] != ss_sorted[i+1]:
                return False

        return True
    else:
        for i in range(0, n-2, 2):
            if ss_sorted[i] != ss_sorted[i + 1] and ss_sorted[i+1] != ss_sorted[i + 2]:
                return False

        return True

if __name__ == '__main__':
    s = "azAZ"
    res = pp(s)
    print(res)