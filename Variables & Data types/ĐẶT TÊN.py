from itertools import combinations

n, k = map(int, input().split())
names = sorted(set(map(str, input().split())))
for x in combinations(names, k):
    print(' '.join(x))

