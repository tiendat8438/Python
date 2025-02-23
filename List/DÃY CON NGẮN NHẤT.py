import math

def find_min_len_subarr(A, N, K):
    min_len = float('inf')
    for i in range(N):
        cur_gcd = 0
        for j in range(i, N):
            cur_gcd = math.gcd(cur_gcd, A[j])
            if cur_gcd == K:
                min_len = min(min_len, j - i + 1)
                break # dừng lại ngay khi tìm thấy do là dãy con ngắn nhất
            elif cur_gcd < K:
                break # Nếu GCD nhỏ hơn K, không thể tiếp tục tìm được dãy con thỏa mãn
    return min_len if min_len != float('inf') else -1

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        while True:
            line = input().strip()
            if line:
                N, K = map(int, line.split())
                break
        A = []
        while len(A) < N:
            line = input().strip()
            if line:
                A.extend(map(int, line.split()))
        # Kiêm tra xem K có phải ước của phần tử nào trong dãy không để tránh tính toán nhiều
        if all(x % K != 0 for x in A):
            print(-1)
            continue
        print(find_min_len_subarr(A, N, K))