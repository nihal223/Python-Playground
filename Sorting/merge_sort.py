def merge_sort(a):
    if len(a) > 1:
        n = len(a)
        mid = n//2

        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        # Merge
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
                k += 1
            else:
                a[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1

    return a


if __name__ == '__main__':
    a = [2,6,4,7,8,3,1,5]
    res = merge_sort(a)
    print(res)