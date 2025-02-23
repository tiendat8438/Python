T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    kernel = [list(map(int, input().split())) for _ in range(3)]
    res = 0
    for i in range(n):
        if i == n - 2: break
        for j in range(m):
            if j == m - 2: break
            for x in range(3):
                for y in range(3):
                    res += kernel[x][y] * mat[i + x][j + y]
    print(res)
    