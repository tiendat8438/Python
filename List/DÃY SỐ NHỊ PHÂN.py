N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    if arr[i] != arr[i + 1]:
        cnt += 1
print(cnt)