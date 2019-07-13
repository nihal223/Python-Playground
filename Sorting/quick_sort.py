def partition(a, l, r):
    i = l-1
    pivot = a[r]
    for j in range(l, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def quick_sort(a, l, r):
    if l < r:
        ind = partition(a, l, r)
        quick_sort(a, 0, ind-1)
        quick_sort(a, ind+1, r)
    return a


if __name__ == '__main__':
    a = [2,6,4,7,8,3,1,5]
    res = quick_sort(a, 0, len(a) - 1)
    print(res)