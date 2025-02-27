class NhanVien:
    def __init__(self, ten, ma, lythuyet, thuchanh):
        self.ten = ten
        self.ma = ma
        self.lythuyet = self.chuan_hoa_diem(lythuyet)
        self.thuchanh = self.chuan_hoa_diem(thuchanh)
        self.tong_diem = (self.lythuyet + self.thuchanh) / 2

    def chuan_hoa_diem(self, diem):
        return diem / 10 if diem > 10 else diem

    def phan_loai(self):
        if self.tong_diem < 5:
            return "TRUOT"
        elif self.tong_diem < 8:
            return "CAN NHAC"
        elif self.tong_diem <= 9.5:
            return "DAT"
        return "XUAT SAC"

    def __lt__(self, other):
        return (self.tong_diem, other.ma) > (other.tong_diem, self.ma)  

if __name__ == "__main__":
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input().strip()
        lythuyet = float(input())
        thuchanh = float(input())
        ma = f'TS{i:03d}'  
        ds.append(NhanVien(ten, ma, lythuyet, thuchanh))
    ds.sort()  
    for nv in ds:
        print(f'{nv.ma} {nv.ten} {nv.tong_diem:.2f} {nv.phan_loai()}')
