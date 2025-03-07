from itertools import permutations

res = permutations(input())
for x in res:
    print(''.join(x))