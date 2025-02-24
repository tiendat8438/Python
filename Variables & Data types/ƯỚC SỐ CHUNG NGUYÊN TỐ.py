from math import gcd

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def tong(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return is_prime(sum)

if __name__ == "__main__":  
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print("YES" if tong(gcd(a, b)) else "NO")