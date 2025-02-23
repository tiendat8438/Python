T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    stack = []
    left = [-1] * (N)
    for i in range(N):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    res = [i - left[i] for i in range(N)]
    print(' '.join(map(str, res)))


