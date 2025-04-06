def solve(A, n):
    if all(A[i] == A[i + 1] for i in range(n - 1)):
        return 1
    max_left, min_right = [0] * (n), [0] * (n)
    max_left[0], min_right[n - 1] = A[0], A[n - 1]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], A[i])
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], A[i])
    cnt = 0
    for i in range(n):
        left_ok = (i == 0 or max_left[i - 1] <= A[i])
        right_ok = (i == n - 1 or min_right[i + 1] > A[i])
        if left_ok and right_ok:
            cnt += 1
    return cnt 


for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    print(solve(A, n))