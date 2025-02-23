def check(a, b, n):
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    print("YES" if check(arrA, arrB, N) else "NO")
