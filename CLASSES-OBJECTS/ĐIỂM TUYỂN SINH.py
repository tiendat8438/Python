class TuyenSinh:
    def __init__(self, ten, ma, diem):
        self.ten = ten
        self.tong_diem = diem
        self.ma = ma

    def tinh_diem(self, khu_vuc, dan_toc):
        if khu_vuc == '1':
            self.tong_diem += 1.5
        elif khu_vuc == '2':
            self.tong_diem += 1.0
        
        if dan_toc != 'Kinh':
            self.tong_diem += 1.5

    def phan_loai(self):
        return "DO" if self.tong_diem >= 20.5 else "TRUOT"

    def __lt__(self, other):
        if self.tong_diem != other.tong_diem:
            return self.tong_diem > other.tong_diem  # Sắp xếp giảm dần
        return self.ma < other.ma  # Nếu bằng nhau, sắp xếp theo mã tăng dần

    def __str__(self):
        return f'{self.ma} {self.ten} {self.tong_diem:.1f} {self.phan_loai()}'

def chuan_hoa_ten(ten):
    return ' '.join(ten.strip().split()).title()

if __name__ == "__main__":
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input().strip()
        diem = float(input().strip())
        dt = input().strip()
        kv = input().strip()
        ma = f'TS{i:02d}'
        
        ts = TuyenSinh(chuan_hoa_ten(ten), ma, diem)
        ts.tinh_diem(kv, dt)
        ds.append(ts)

    ds.sort()
    
    for x in ds:
        print(x)
