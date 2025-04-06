def is_rev(n):
    s = str(n)
    return s == s[::-1]

def to_base(n, base):
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits if digits else [0]

def solve(a, b, m):
    cnt = 0
    for i in range(a, b + 1):
        for base in range(2, m + 1):
            if not is_rev(to_base(i, base)):
                break
            else:
                cnt += 1
    return cnt

a, b, m = map(int, input().split())
print(solve(a, b, m))