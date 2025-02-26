import sys

class ThiSinh:
    def __init__(self, ten, date, diem1, diem2, diem3):
        self.ten = ten
        self.date = date
        self.a = float(diem1)
        self.b = float(diem2)
        self.c = float(diem3)
    def tong_diem(self):
        return self.a + self.b + self.c
    def __str__(self):
        return f'{self.ten} {self.date} {self.tong_diem():.1f}'
    
if __name__ == "__main__":
    data = sys.stdin.read().splitlines()  # Đọc dữ liệu và tách dòng
    ten, date = data[:2]
    diem1, diem2, diem3 = map(float, data[2:])  # Chuyển đổi điểm sang float

    p = ThiSinh(ten, date, diem1, diem2, diem3)
    print(p)
