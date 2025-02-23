from collections import Counter

s = input()
A = [s[i:i+2] for i in range(0, len(s) - 1, 2)]
counter = Counter(A)
for key, val in counter.items():
    print(f'{key} {val}')  