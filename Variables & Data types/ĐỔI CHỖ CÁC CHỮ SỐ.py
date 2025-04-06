def solve(n):
    n = list(n)
    idx = -1
    for i in range(len(n) - 1, 0, -1):
        if n[i - 1] > n[i]:
            idx = i - 1
            break
    if idx == -1:
        return -1
    swap_idx = idx + 1
    for j in range(idx + 1, len(n)):
        if n[j] < n[idx] and n[j] > n[swap_idx]:
            swap_idx = j
    n[idx], n[swap_idx] = n[swap_idx], n[idx]
    return ''.join(n) if n[0] != '0' else -1

for _ in range(int(input())):
    n = input()
    print(solve(n))