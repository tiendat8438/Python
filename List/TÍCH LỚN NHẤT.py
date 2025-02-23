n = int(input())
A = sorted(list(map(int, input().split())))
ans2, ans3 = A[-1]*A[-2], A[-1]*A[-2]*A[-3]
ans2 = max(ans2, A[0]*A[1])
ans3 = max(ans3, A[0]*A[1]*A[-1])
print(max(ans2, ans3))