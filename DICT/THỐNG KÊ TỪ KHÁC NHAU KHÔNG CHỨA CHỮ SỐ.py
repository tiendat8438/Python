import re
from collections import Counter

txt = []
n = int(input())
for _ in range(n):
    line = input()
    # Loại bỏ các chữ số trong dòng
    line_without_digits = re.sub(r'\d', '', line)
    # Tách từ và chuyển đổi thành chữ thường
    words = re.findall(r'\b\w+\b', line_without_digits.lower())
    txt.extend(words)
counter = Counter(txt)
sorted_list = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
for key, val in sorted_list:
    print(f'{key} {val}')