def is_palindromic(n):
    str_n = str(n)
    if len(str_n) < 2:
        return False
    return str_n == str_n[::-1]

def find_max(n, m, mat):
    palin_nums = [mat[i][j] for i in range(n) for j in range(m) if is_palindromic(mat[i][j])]
    if not palin_nums:
        return "NOT FOUND", []
    max_palin = max(palin_nums)
    res = [(i, j) for i in range(n) for j in range(m) if mat[i][j] == max_palin]
    return max_palin, res

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
max_palins, res = find_max(n, m, mat)
if max_palins == "NOT FOUND":
    print("NOT FOUND")
else:
    print(max_palins)
    for i, j in res:
        print(f'Vi tri [{i}][{j}]')
