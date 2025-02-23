def gt(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def is_krish(n):
    sum = 0
    tmp = n
    while n > 0:
        sum += gt(n % 10)
        n //= 10
    return bool(sum == tmp)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        print('Yes' if is_krish(n) else 'No')
