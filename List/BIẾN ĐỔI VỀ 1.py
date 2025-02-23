from collections import deque

# def bfs(N):
#     queue = deque([(N, 1)])
#     visited = set()
#     visited.add(N)
#     while queue:
#         cur, cnt = queue.popleft()
#         if cur == 1:
#             return cnt
#         if cur % 2 == 0 and (cur // 2) not in visited:
#             visited.add(cur // 2)
#             queue.append((cur // 2, cnt + 1))
#         if cur % 2 == 1 and (cur * 3 + 1) not in visited:
#             visited.add(cur * 3 + 1)
#             queue.append((cur * 3 + 1, cnt + 1))
#     return -1

def count(N):
    vals = set()
    vals.add(N)
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = N * 3 + 1
        vals.add(N)
    return len(vals)

if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        print(count(N))

