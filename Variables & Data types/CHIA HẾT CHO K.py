def find_b(a, n, k):
    x = a + (k - a % k) % k
    b = x - a
    if b > n - a:
        print(-1)
        return
    res = [i for i in range(b, n - a + 1, k) if i != 0]
    if res:
        print(' '.join(map(str, res)))
    else:
        print(-1)

a, k, n = map(int, input().split())
find_b(a, n, k)
