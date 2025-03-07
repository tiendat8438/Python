from math import isqrt

def isPrime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES" if isPrime(int(s[-4:])) else "NO")
