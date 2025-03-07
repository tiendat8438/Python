from collections import deque

def bfs(A, n, m):
    q = deque()
    ans = [[0]*m for i in range(n)]
    q.append((0,0))
    while len(q):
        i, j = q.popleft()
        if i == n - 1 and j == m - 1:
            return ans[i][j]
        if i<n-1:
            d = abs(A[i+1][j] - A[i][j])
            if d and i + d < n and ans[i+d][j] == 0:
                ans[i+d][j] = ans[i][j]+1
                q.append((i+d, j))
        if j<m-1:
            r = abs(A[i][j+1] - A[i][j])
            if r and j + r < m and ans[i][j+r] == 0:
                ans[i][j+r] = ans[i][j]+1
                q.append((i, j+r))
        if i<n-1 and j<m-1:
            dr = abs(A[i+1][j+1] - A[i][j])
            if dr and i+dr<n and j+dr<m and ans[i+dr][j+dr] == 0:
                ans[i+dr][j+dr] = ans[i][j] + 1
                q.append((i+dr, j+dr))
    return ans[n - 1][m - 1] if ans[n - 1][m - 1] else -1

for t in range(int(input())):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    print(bfs(A, n, m))
    