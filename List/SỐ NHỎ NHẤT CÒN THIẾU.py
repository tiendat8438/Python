N = int(input())
A = list(map(int, input().split()))
daxet = [False] * (N + 1)
for num in A:
    if 1 <= num <= N:
        daxet[num] = True

for i in range(1, N + 1):
    if not daxet[i]:
        print(i)
        break
else:
    print(N + 1)
