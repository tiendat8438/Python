# Số điểm nguyên trên cạnh của đa giác
"""Một đoạn thẳng giữa hai điểm nguyên (x1, y1) và (x2, y2) có số lượng điểm nguyên nằm trên đoạn
    đó (bao gồm cả hai đầu mút) bằng ước chung lớn nhất (gcd) của độ dài theo trục x và y, cộng thêm 1:
    Số điểm nguyên trên cạnh (x1, y1) đến (x2, y2) = gcd(|x2 - x1|, |y2 - y1|) + 1
"""
# Số lượng điểm nguyên nằm trong đa giác
"""Dựa vào định lý pick:
    A = m + k//2 - 1
    A  là diện tích của đa giác (có thể tính bằng công thức Shoelace).
    k là số điểm nguyên trên cạnh.
    m là số điểm nguyên bên trong đa giác.
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# Tính diện tích bằng công thức shoelace
def shoelace_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1*y2 - x2*y1
    return abs(area) // 2

def count_boundary_points(points):
    n = len(points)
    cnt = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        cnt += gcd(abs(x2 - x1), abs(y2 - y1))
    return cnt

with open('INPUT.TXT', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    points = [tuple(map(int, file.readline().strip().split())) for _ in range(n)]

area = shoelace_area(points)
k = count_boundary_points(points)
m = area - k//2 + 1

with open('OUTPUT.TXT', 'w', encoding='utf-8') as file:
    file.write(f'{k} {m}\n')

