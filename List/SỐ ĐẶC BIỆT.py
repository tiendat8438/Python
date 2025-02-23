MOD = 10**9 + 7

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    res = 0
    pow = 1
    while k > 0:
        if k % 2 == 1:
            res = (res + pow) % MOD
        pow = (pow * n) % MOD
        k //= 2
    print(res)