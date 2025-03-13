from math import gcd

def min_cost_to_reach_anywhere(n, a, c):
    MAX_GCD = 10**9  # Giá trị lớn nhất của a[i]
    
    # Tạo một dictionary để lưu chi phí tối thiểu cho từng GCD
    dp = {0: 0}  # GCD=0 không có nghĩa
    for i in range(n):
        ai, ci = a[i], c[i]
        new_dp = dp.copy()  # Tạo một bản sao để cập nhật
        
        for g, cost in dp.items():
            new_gcd = gcd(g, ai)
            if new_gcd not in new_dp or new_dp[new_gcd] > cost + ci:
                new_dp[new_gcd] = cost + ci
        
        dp = new_dp  # Cập nhật trạng thái
        
    return dp[1] if 1 in dp else -1  # Trả về chi phí tối thiểu đạt GCD=1

# Đọc input
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(min_cost_to_reach_anywhere(n, a, c))
