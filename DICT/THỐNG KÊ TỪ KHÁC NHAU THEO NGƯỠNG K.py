import re
from collections import Counter

txt = []
n, k = map(int, input().split())
for _ in range(n):
    line = input()
    x = re.findall(r'\b\w+\b', line.lower())
    txt.extend(x)
counter = Counter(txt)
sorted_list = sorted(counter.items(), key=lambda x : (-x[1], x[0]))
for key, val in sorted_list:
    if val >= k:
        print(f'{key} {val}')