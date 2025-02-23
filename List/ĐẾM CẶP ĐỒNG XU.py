n = int(input())
mat = [list(map(str, input())) for _ in range(n)]
cnt = 0
for row in mat:
    count_C = row.count('C')
    cnt += count_C*(count_C - 1)//2
for col in range(n):
    count_C = sum(1 for row in mat if row[col] == 'C')
    cnt += count_C*(count_C - 1)//2
print(cnt)