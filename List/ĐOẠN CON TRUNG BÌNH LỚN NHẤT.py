from itertools import groupby

n = int(input())
A = list(map(int, input().split()))
max_num = max(A)

print(max(len(list(g)) for k, g in groupby(A) if k == max_num))



