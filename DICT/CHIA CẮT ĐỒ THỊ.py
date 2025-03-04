from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_count_cmps(self, removed_node):
        """ Đếm số thành phần liên thông khi loại bỏ removed_node """
        visited = [False] * (self.n + 1)
        cnt = 0

        def bfs(start):
            queue = [start]
            visited[start] = True
            while queue:
                node = queue.pop(0)
                for v in self.graph[node]:
                    if not visited[v] and v != removed_node:
                        visited[v] = True
                        queue.append(v)
        for i in range(1, n + 1):
            if not visited[i] and i != removed_node:
                cnt += 1
                bfs(i)
        return cnt
    
    def find_node_to_remove(self):
        """ Tìm đỉnh quan trọng nhất để xóa """
        # Số thành phần liên thông ban đầu
        max_cmps = self.bfs_count_cmps(-1)
        best_node = 0
        for u in range(1, self.n + 1):
            new_cmps = self.bfs_count_cmps(u)
            if new_cmps > max_cmps:
                max_cmps = new_cmps
                best_node = u
            elif new_cmps == max_cmps:
                best_node = min(u, best_node)
        return best_node
        

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = Graph(n)
        for _ in range(m):
            u, v = map(int, input().split())
            g.add_edges(u, v)
        print(g.find_node_to_remove())
