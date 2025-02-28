from collections import defaultdict, deque

def kahn(n, data):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for a, sign, b in data:
        if sign == '>':
            graph[a].append(b)
            in_degree[b] += 1
        else:
            graph[b].append(a)
            in_degree[b] += 1
    cnt = 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    while queue:
        cur = queue.popleft()
        cnt += 1
        for v in graph[cur]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if cnt < len(in_degree):
        return "impossible"
    return "possible"

if __name__ == "__main__":
    n = int(input())
    data = [input().split() for _ in range(n)]
    print(kahn(n, data))
