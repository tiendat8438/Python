with open('INPUT.TXT', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    segment = []
    for _ in range(n):
        a, b = map(int, file.readline().strip().split())
        segment.append((a, b))

segment.sort()
total = 0
cur_start, cur_end = segment[0]

for i in range(1, n):
    a, b = segment[i]
    if a <= cur_end:
        cur_end = max(cur_end, b)
    else:
        total += cur_end - cur_start
        cur_start, cur_end = a, b

total += cur_end - cur_start

with open("OUTPUT.TXT", 'w', encoding='utf-8') as file:
    file.write(str(total) + '\n')