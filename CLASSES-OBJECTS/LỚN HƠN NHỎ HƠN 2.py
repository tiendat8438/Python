from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề
        self.in_degree = defaultdict(int)  # Số bậc vào

    def add_edge(self, a, b):
        """ Thêm cạnh a → b vào đồ thị """
        self.graph[a].append(b)
        self.in_degree[b] += 1
        # Đảm bảo tất cả các đỉnh có trong in_degree
        if a not in self.in_degree:
            self.in_degree[a] = 0

    def is_possible(self):
        """ Kiểm tra đồ thị có chu trình hay không (Thuật toán Kahn) """
        queue = deque([node for node in self.in_degree if self.in_degree[node] == 0])
        count = 0  # Số đỉnh đã xử lý

        while queue:
            u = queue.popleft()
            count += 1
            for v in self.graph[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)

        # Nếu xử lý hết các đỉnh → Không có chu trình → possible
        if count == len(self.in_degree):
            return "possible"
        return "impossible"

# Đọc input
n = int(input().strip())
graph = Graph()

# Thêm cạnh vào đồ thị
for _ in range(n):
    a, sign, b = input().strip().split()
    if sign == ">":
        graph.add_edge(a, b)  # a > b → a → b
    else:
        graph.add_edge(b, a)  # a < b → b → a

# Kiểm tra chu trình
print(graph.is_possible())