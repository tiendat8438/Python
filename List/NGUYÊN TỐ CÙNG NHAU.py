import math

N = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(N - 1):
    for j in range(i + 1, N):
        if math.gcd(A[i], A[j]) == 1:
            print(A[i], A[j])