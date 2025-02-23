T = int(input())
for _ in range(T):
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [float('inf')] * (n + 1) # dp[i] là thời gian ít nhất để tạo ra i kí tự
    dp[0] = 0
    dp[1] = x
    for i in range(2, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + x)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + z) # Copy từ i/2
            dp[i] = min(dp[i], dp[(i//2) + 1] + y + z) # Copy từ i/2 + 1 rồi xóa đi 1 kí tự
        else:
            dp[i] = min(dp[i], dp[(i - 1)//2] + x + z)
            dp[i] = min(dp[i], dp[(i + 1)//2] + y + z)
    print(dp[n])
