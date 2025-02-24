for _ in range(int(input())):
    n = int(input())
    res = 0
    if n % 2 == 1:
        res = sum(1/i for i in range(1, n + 1, 2))
    else:
        res = sum(1/i for i in range(2, n + 1, 2))
    print(f'{res:.6f}')