from math import sqrt

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes, is_prime

def min_steps_to_prime(n, a):
    limit = 110000
    primes, is_prime = sieve(limit)
    max_steps = 0
    for num in a:
        min_steps = float('inf')
        for prime in primes:
            if prime > num + max_steps:  # Không cần kiểm tra các số quá xa
                break
            min_steps = min(min_steps, abs(num - prime))
        max_steps = max(max_steps, min_steps)
    
    return max_steps

n = int(input())
a = list(map(int, input().split()))
print(min_steps_to_prime(n, a))