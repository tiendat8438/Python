MOD = 10 ** 9 + 7

def lt(x, k):
    res = 1
    x = x % MOD
    while k > 0:
        if k % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        k //= 2
    return res

if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        res = 0
        for i in range(1, n + 1):
            res = (res + lt(i, k)) % MOD
        print(res)
    