def check(a, n):
    for i in range(1, n):
        if a[i] == a[i - 1]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(a, n))