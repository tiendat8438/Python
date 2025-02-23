T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        a, b = A[i], A[i + 1]
        if a > b:
            a, b = b, a
        while 2 * a < b:
            a *= 2
            cnt += 1
    print(cnt)