from collections import defaultdict, deque

def kahn(n, data):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Xây dựng đồ thị
    all_nodes = set()
    for a, sign, b in data:
        all_nodes.update([a, b])  # Lưu tất cả các đỉnh
        if sign == '>':
            graph[a].append(b)
            in_degree[b] += 1
        else:
            graph[b].append(a)
            in_degree[a] += 1
    
    # Đảm bảo tất cả các đỉnh đều có trong in_degree
    for node in all_nodes:
        if node not in in_degree:
            in_degree[node] = 0
    
    # Thuật toán Kahn
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    cnt = 0

    while queue:
        cur = queue.popleft()
        cnt += 1
        for v in graph[cur]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Nếu có chu trình thì trả về "impossible"
    if cnt < len(all_nodes):  
        return "impossible"
    return "possible"

# Nhập input và chạy thuật toán
if __name__ == "__main__":
    n = int(input().strip())
    data = [input().split() for _ in range(n)]
    print(kahn(n, data))
