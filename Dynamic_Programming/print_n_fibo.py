import time

def fibo(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]


def all_fibo(n):
    memo = [-1]*(n+1)
    for i in range(n):
        print(i+1, ':', fibo(i+1, memo))

start_time = time.time()
all_fibo(100)
print("--- %s seconds ---" % (time.time() - start_time))