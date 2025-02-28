A = list(map(int, input().split()))
res = []
for i in range(1, len(A)):
    if A[i] > A[i - 1]:
        res.append(A[i])
    else:
        continue
print(*res)