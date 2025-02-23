def is_lucky(n, m, mat):
    dif = max(map(max, mat)) - min(map(min, mat))
    lucky_nums = [mat[i][j] for i in range(n) for j in range(m) if mat[i][j] == dif]
    if not lucky_nums:
        return 'NOT FOUND', []
    max_num = max(lucky_nums)
    res = [(i, j) for i in range(n) for j in range(m) if mat[i][j] == max_num]
    return max_num, res
    
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
max_num, res = is_lucky(n, m, mat)
if max_num == 'NOT FOUND':
    print("NOT FOUND")
else:
    print(max_num)
    for i, j in res:
        print(f'Vi tri [{i}][{j}]')