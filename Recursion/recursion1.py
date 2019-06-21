def f(n):
    print(n)
    if n <= 1:
        return 1

    return f(n-1) + f(n-1)

x = f(4)
print(x)