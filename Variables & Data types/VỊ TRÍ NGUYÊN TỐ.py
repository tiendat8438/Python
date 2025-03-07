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

def solve(s):
    for i in range(0, len(s)):
        tmp = ord(s[i]) - ord('0')
        if isPrime(i) and not isPrime(tmp):
            return 'NO'
        elif not isPrime(i) and isPrime(tmp):
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    s = input()
    print(solve(s))