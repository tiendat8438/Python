import math

def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = int(n / 10)
    return rev

def find_emirp(n):
    isprime = [True] * (n + 1)
    isprime[0] = isprime[1] = False
    p = 2
    while p * p <= n:
        if isprime[p]:
            for j in range(p * 2, n + 1, p):
                isprime[j] = False
        p += 1

    for p in range(2, n + 1):
        if isprime[p]:
            rev = reverse(p)
            if rev != p and rev <= n and isprime[rev]:
                print(p, rev, end = ' ')
                isprime[rev] = False

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        find_emirp(n)
        print()
