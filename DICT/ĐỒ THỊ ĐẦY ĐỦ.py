n, m = int(input()), int(input())
zone = []  # Danh sách các nhóm đỉnh có liên kết với nhau
ke = [[0]*(n+1) for i in range(n+1)]  # Ma trận kề để lưu thông tin đồ thị (0 là không có cạnh, 1 là có cạnh).
par = [-1]*(n+1) # Mảng đánh dấu đỉnh thuộc nhóm nào

for i in range(m):
    x, y = map(int, input().split())  # Đọc 2 đỉnh của cạnh
    ke[x][y] = ke[y][x] = 1  # Đánh dấu có cạnh giữa x và y
    p = par[x] if par[y] == -1 else par[y]  # Xác định nhóm của đỉnh
    if p == -1:  # Nếu cả hai đỉnh chưa thuộc nhóm nào
        zone.append(set([x, y]))  # Tạo nhóm mới chứa x, y
        par[x] = par[y] = len(zone) - 1  # Đánh dấu nhóm của x và y
    else:  # Nếu ít nhất một trong hai đã có nhóm
        zone[p].add(x)
        zone[p].add(y)
        par[x] = par[y] = p

def check():
    for z in zone:  # Duyệt qua từng vùng (tập hợp các đỉnh)
        for x in z:
            for y in z:
                if x != y:
                    if ke[x][y] == 0 or ke[y][x] == 0:  # Nếu tồn tại một cặp đỉnh trong vùng không có cạnh nối
                        return False
    return True
if check(): print('YES')
else: print('NO')