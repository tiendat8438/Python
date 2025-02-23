def min_steps(A, n):
    min_steps = float('inf')
    for i in range(n):
        target = [0]*n
        target[i] = A[i]

        for j in range(i - 1, -1, -1):
            target[j] = max(target[j + 1] - 1, 1)
        for j in range(i + 1, n):
            target[j] = max(target[j - 1] - 1, 1)

        steps = sum(abs(A[j] - target[j]) for j in range(n))
        min_steps = min(min_steps, steps)
    return min_steps

n = int(input())
A = list(map(int, input().split()))
print(min_steps(A, n))

