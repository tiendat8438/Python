T = int(input())
for _ in range(T):
    n = int(input())
    A, B = [], []
    for i in range(n):
        x, y = map(float, input().split())
        A.append(x)
        B.append(y)
    dp = [1] * n # Dãy con hợp lệ dài nhất kết thúc ở i
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and B[i] < B[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
    