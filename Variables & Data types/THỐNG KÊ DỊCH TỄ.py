def bfs(A, n, m):
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = [[False for _ in range(m)] for _ in range(n)]  
    cnt = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == -1:
                for dx, dy in dir:
                    x, y = i + dx, j + dy       
                    if 0 <= x < n and 0 <= y < m and A[x][y] != 0 and not visited[x][y]:
                        cnt += A[x][y]
                        visited[x][y] = True  
    return cnt

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(bfs(A, n, m))