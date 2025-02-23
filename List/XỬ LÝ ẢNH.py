def solve(n, m, l, mat):
    k = (l - 1) // 2
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i][j]
    A = []
    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            h1, h2, c1, c2 = i, i + l - 1, j, j + l - 1
            sum = prefix[h2][c2] - prefix[h1 - 1][c2] - prefix[h2][c1 - 1] + prefix[h1 - 1][c1 - 1]
            A[i][j] = sum
    res = [[0] * (m - l + 2) for _ in range(n - l + 2)]
    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            res.append(A[i][j])
    return res

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m, l = map(int, input().split())
        mat = [list(map(int, input().split())) * (m + 1) for _ in range(1, n + 1)]
        res = solve(n, m, l, mat)
        print('\n'.join(' '.join(map(str, row)) for row in res))

        