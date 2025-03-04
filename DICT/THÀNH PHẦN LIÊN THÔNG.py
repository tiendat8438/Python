def dfs(adj, u, visited):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(adj, v, visited)

if __name__ == "__main__":
    n, m, x = map(int, input().split())
    adj = {i : [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (n + 1)
    dfs(adj, x, visited)
    nodes = [i for i in range(1, n + 1) if not visited[i]]
    if nodes:
        for v in nodes:
            print(v)
    else:
        print(0)