def powers_of_2(n):
    if n <= 0:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powers_of_2(int(n/2))
        curr = prev * 2
        print(curr)
        return curr

powers_of_2(50)