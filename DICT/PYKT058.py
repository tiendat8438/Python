def dinh_that(adj, start, end, vertex_remove, n):
    queue = [start]
    visited = [False] * (n + 1)
    visited[start] = 1
    while queue:
        cur = queue.pop()
        if cur == end:
            return False
        for v in adj[cur]:
            if not visited[v] and v != vertex_remove:
                queue.append(v)
                visited[v] = True
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, u, v = map(int, input().split())
        adj = {i : [] for i in range(1, n + 1)}
        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)
        cnt = 0
        for i in range(1, n + 1):
            if i != u and i != v:
                if dinh_that(adj, u, v, i, n):
                    cnt += 1
        print(cnt)

