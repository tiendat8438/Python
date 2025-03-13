from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Kiểm tra các số dạng 6k ± 1 từ 5 đến √n
    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def count(n):
    cnt = 0
    # Trường hợp 1: p^8
    max_p = int(n ** (1/8)) + 1
    for p in range(max_p):
        if is_prime(p):
            if p ** 8 <= n:
                cnt += 1
    # Trường hợp 2: p^2 * q^2
    max_pq = int(n ** 0.5) + 1
    primes = [p for p in range(2, max_pq) if is_prime(p)]
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p = primes[i]
            q = primes[j]
            if p*q <= max_pq:
                if (p**2) * (q**2) <= n:
                    cnt += 1

    return cnt

print(count(int(input())))