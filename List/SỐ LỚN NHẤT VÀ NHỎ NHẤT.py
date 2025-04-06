MOD = 10**9 + 7

# Tính toán các giá trị của tổ hợp bằng quy hoạch động
def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return (fact[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD

# Tính toán và lưu trữ các giá trị của giai thừa và nghịch đảo giai thừa
def precompute_factorials(max_n, MOD):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    return fact, inv_fact

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # Nếu K = 1, kết quả là 0
    if K == 1:
        print(0)
        return
    # Tính toán các giá trị giai thừa và nghịch đảo giai thừa
    max_n = N
    fact, inv_fact = precompute_factorials(max_n, MOD)
    # Tính tổng chênh lệch
    total = 0   
    # Tính tổng A[j] * C(j, K-1) với j từ K-1 đến N-1
    sum_max = 0
    for j in range(K-1, N):
        sum_max = (sum_max + A[j] * comb(j, K-1, fact, inv_fact)) % MOD
    # Tính tổng A[i] * C(N - i - 1, K - 1) với i từ 0 đến N-K
    sum_min = 0
    for i in range(N - K + 1):
        sum_min = (sum_min + A[i] * comb(N - i - 1, K - 1, fact, inv_fact)) % MOD   
    # Kết quả là sum_max - sum_min
    total = (sum_max - sum_min) % MOD
    print(total)

if __name__ == "__main__":
    main()