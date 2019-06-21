import time

def is_perm(s1,s2):
    if(len(s1) != len(s2)):
        return False

    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    for i in range(len(sorted_s1)):
        if sorted_s1[i] != sorted_s2[i]:
            return False

    return True


if __name__ == '__main__':
    s1 = 'abcd'
    s2 = 'lwen'

    start_time = time.time()
    res = is_perm(s1,s2)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(res)

