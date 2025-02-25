from math import sqrt

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def is_valid(self):
        # Kiểm tra điều kiện 3 điểm thẳng hàng
        return (self.x2 - self.x1) * (self.y3 - self.y1) != (self.x3 - self.x1) * (self.y2 - self.y1)

    def distance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def dientich(self):
        if not self.is_valid():
            return "INVALID"
        
        AB = self.distance(self.x1, self.y1, self.x2, self.y2)
        BC = self.distance(self.x2, self.y2, self.x3, self.y3)
        CA = self.distance(self.x3, self.y3, self.x1, self.y1)

        # Công thức Heron chuẩn
        s = (AB + BC + CA) / 2
        area = sqrt(s * (s - AB) * (s - BC) * (s - CA))

        return f"{area:.2f}"

if __name__ == "__main__":
    n = int(input())  # Số bộ test
    data = []
    # Đọc input trên nhiều dòng
    while len(data) < 6 * n:
        line = input().strip()
        if line:
            data.extend(map(float, line.split()))

    for i in range(n):
        x1, y1, x2, y2, x3, y3 = data[i * 6:(i + 1) * 6]
        p = Triangle(x1, y1, x2, y2, x3, y3)
        print(p.dientich())
