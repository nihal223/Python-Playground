def pair_sum(a, b):
    print("Summing {} and {}".format(a,b))
    return (a+b)

def pair_sum_sequence(n):
    sum = 0
    for i in range(n):
        sum += pair_sum(i, i+1)
    return sum

if __name__=='__main__':
    result = pair_sum_sequence(10)
    print(result)
