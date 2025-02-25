from math import sqrt

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def is_valid(self):
        # Kiểm tra điều kiện thẳng hàng
        return (self.x2 - self.x1) * (self.y3 - self.y1) != (self.x3 - self.x1) * (self.y2 - self.y1)

    def distance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def chuvi(self):
        if not self.is_valid():
            return "INVALID"
        AB = self.distance(self.x1, self.y1, self.x2, self.y2)
        BC = self.distance(self.x2, self.y2, self.x3, self.y3)
        CA = self.distance(self.x3, self.y3, self.x1, self.y1)
        return f'{AB+BC+CA:.3f}'

if __name__ == "__main__":
    res = []       
    n = int(input())  # Nhập số bộ test
    data = []
    # Đọc input cho đến khi đủ 6 * n số
    while len(data) < 6 * n:
        line = input().strip()
        if line:
            data.extend(map(int, line.split()))  # Thêm tất cả số từ dòng hiện tại

    # Chia dữ liệu thành từng bộ test 6 số một
    for i in range(n):
        x1, y1, x2, y2, x3, y3 = data[i * 6:(i + 1) * 6]
        p = Triangle(x1, y1, x2, y2, x3, y3)
        res.append(p.chuvi())

    for x in res:
        print(x)
