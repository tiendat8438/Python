import sys
import math

is_prime = [True] * (10**6 + 1)

def sieve():
    is_prime[0] = is_prime[1] = False
    for i in range(2, math.isqrt(10**6)):
        if is_prime[i]:
            for j in range(i*i, 10**6 + 1, i):
                is_prime[j] = False
    primes = [i for i in range(10**6 + 1) if is_prime[i]]
    return primes

def count(n, primes):
    cnt = 0
    for p in primes:
        if p + 6 >= n:
            break
        if (p + 2 in primes and p + 6 in primes) or  (p + 4 in primes and p + 6 in primes):
            cnt += 1
    return cnt

if __name__ == '__main__':
    primes = sieve()
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        print(count(n, primes))