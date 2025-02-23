n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
if n == m:
    res = mat
else:
    if n > m:
        dif = n - m # số hàng cần xóa
        odd_row_ids = [i for i in range(n) if (i + 1) % 2 == 1] # đánh dấu chỉ số những hàng lẻ
        remove_rows = odd_row_ids[:dif] 
        res = [mat[i] for i in range(n) if i not in remove_rows]
    else:
        dif = m - n # số cột cần xóa
        even_col_ids = [i for i in range(m)  if (i + 1) % 2 == 0] # đánh dấu chỉ số cột chẵn
        remove_cols = even_col_ids[:dif]
        res = []
        for row in mat:
            new_row = [row[j] for j in range(m) if j not in remove_cols]
            res.append(new_row)

for row in res:
    print(*row)