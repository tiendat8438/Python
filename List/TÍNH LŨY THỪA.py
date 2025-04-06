import math

# Hàm tính lũy thừa nhanh (a^b mod m)
def fast_exponentiation(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2
    return result

# Hàm tính LCM của hai số
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Hàm tính hàm Carmichael λ(M)
def carmichael(m):
    if m == 1:
        return 1
    factors = {}
    temp = m
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            cnt = 0
            while temp % p == 0:
                temp //= p
                cnt += 1
            factors[p] = cnt
        p += 1
    if temp > 1:
        factors[temp] = 1
    lambda_m = 1
    for p, exp in factors.items():
        if p == 2 and exp >= 3:
            lambda_m = lcm(lambda_m, 2 ** (exp - 2))
        else:
            lambda_m = lcm(lambda_m, (p - 1) * (p ** (exp - 1)))
    return lambda_m

# Hàm xử lý mỗi test case
def solve():
    # Đọc số lượng test case T
    T = int(input())
    for _ in range(T):
        # Đọc a, b, c, d, M
        a, b, c, d, M = map(int, input().split())
        
        # Nếu M = 1, kết quả luôn là 0
        if M == 1:
            print(0)
            continue
        
        # Tính λ(M)
        lambda_M = carmichael(M)
        
        # Tính c^d mod λ(M)
        if lambda_M == 0:
            exp = 0
        else:
            exp = fast_exponentiation(c, d, lambda_M)
        
        # Tính b * (c^d mod λ(M))
        total_exp = b * exp
        
        # Tính a^(b * (c^d mod λ(M))) mod M
        if a == 0:
            print(0)
        else:
            result = fast_exponentiation(a, total_exp, M)
            print(result)

if __name__ == "__main__":
    solve()