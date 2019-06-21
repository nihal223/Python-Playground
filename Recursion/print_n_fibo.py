import time
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


def all_fibo(n):
    for i in range(n):
        print(i+1, ':', fibo(i+1))

start_time = time.time()
all_fibo(30)
print("--- %s seconds ---" % (time.time() - start_time))