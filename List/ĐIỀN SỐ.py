T = int(input())
for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    minval, maxval = min(A), max(A)
    cnt = sum(1 for i in range(minval, maxval + 1) if i not in A)
    print(cnt)
