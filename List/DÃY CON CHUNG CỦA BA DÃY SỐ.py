from collections import Counter

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    A = Counter(map(int, input().split()))
    B = Counter(map(int, input().split()))
    C = Counter(map(int, input().split()))

    res = []
    for num in A:
        if num in B and num in C:
            min_count = min(A[num], B[num], C[num])
            res.extend([num] * min_count)

    if res:
        print(*res)
    else:
        print("NO")