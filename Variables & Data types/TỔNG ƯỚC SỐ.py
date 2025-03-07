import sys
import math

def sieve(max_num):
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if sieve[i]:
            for j in range(i*i, max_num+1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def prime_factors(n, primes):
    factors = []
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            factors.append(p)
            n = n // p
    if n > 1:
        factors.append(n)
    return factors

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    numbers = list(map(int, data[1:N+1]))
    
    max_num = max(numbers)
    primes = sieve(max_num)
    
    total = 0
    for num in numbers:
        factors = prime_factors(num, primes)
        total += sum(factors)
    
    print(total)

if __name__ == "__main__":
    main()