from itertools import permutations

def sinh(n):
    nums = list(range(1, n + 1))
    all_permutations = sorted(permutations(nums), reverse=True)
    print(len(all_permutations))
    for x in all_permutations:
        print(''.join(map(str, x)), end=' ')
    print()

T = int(input())
for _ in range(T):
    n = int(input())
    sinh(n)