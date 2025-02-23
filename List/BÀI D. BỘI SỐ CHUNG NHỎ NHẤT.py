from collections import defaultdict

MOD = 10**9 + 7
MAX_N = 10**6

# Bước 1: Tiền xử lý Sàng Eratosthenes
spf = list(range(MAX_N + 1))  # Mảng smallest prime factor (spf)

for i in range(2, int(MAX_N ** 0.5) + 1):
    if spf[i] == i:  # Nếu i là số nguyên tố
        for j in range(i * i, MAX_N + 1, i):
            if spf[j] == j:
                spf[j] = i  # Đánh dấu ước số nguyên tố nhỏ nhất

# Hàm phân tích thừa số nguyên tố dựa vào spf (O(log n))
def get_prime_factors(n):
    factors = defaultdict(int)
    while n > 1:
        factors[spf[n]] += 1
        n //= spf[n]
    return factors

# Bước 2: Đọc input và xử lý
def count_lcm_pairs(a, b):
    # Dùng defaultdict để lưu số mũ của từng thừa số nguyên tố
    prime_factors = defaultdict(int)
    # Sàng trên đoạn [a, b]
    for i in range(a, b + 1):
        factors = get_prime_factors(i)
        for p, e in factors.items():
            prime_factors[p] += e  # Cộng dồn số mũ

    # Bước 3: Tính số cặp (x, y)
    result = 1
    for e in prime_factors.values():
        result = (result * (2 * e + 1)) % MOD

    return result

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(count_lcm_pairs(a, b))