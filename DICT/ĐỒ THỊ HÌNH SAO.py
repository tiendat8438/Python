from collections import defaultdict

def is_star_graph(n, edges):
    if n == 1:
        return "Yes"
    degree = defaultdict(int)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    max_degree = max(degree.values())
    # Để là hình sao, phải có một đỉnh có bậc (N-1) và các đỉnh còn lại có bậc 1
    if max_degree == n - 1 and list(degree.values()).count(1) == n - 1:
        return "Yes"
    return "No"

if __name__ == "__main__":
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(is_star_graph(n, edges))