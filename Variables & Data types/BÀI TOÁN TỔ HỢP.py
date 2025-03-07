from itertools import combinations

n, k = map(int, input().split())
A = sorted(set(map(int, input().split())))
res = combinations(A, k)
for x in res:
    print(' '.join(map(str, x)))