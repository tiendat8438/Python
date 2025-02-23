def recoverA(B, n):
    if n == 2:
        return (1, B[0][1] - 1)
    A = [0] * n
    A[0] = (B[0][1] + B[0][2] - B[1][2]) // 2
    for i in range(1, n):
        A[i] = B[0][i] - A[0]
    return A


n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]
A = recoverA(B, n)
print(' '.join(map(str, A)))