n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
upper_A = [A[i][j] for i in range(n) for j in range(n) if i + j < n - 1]
lower_A = [A[i][j] for i in range(n) for j in range(n) if i + j > n - 1]
res = abs(sum(upper_A) - sum(lower_A))
if res <= k:
    print("YES")
else:
    print("NO")
print(res)

