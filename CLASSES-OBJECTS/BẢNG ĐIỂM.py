class BangDiem:
    def __init__(self, ten, ma):
        self.ten = ten
        self.ma = ma
        self.tong_diem = 0.0

    def diem_trung_binh(self, toan, tv, nn, vl, hh, sh, ls, dl, gdcd, cn):
        self.tong_diem += ((toan*2 + tv*2 + nn + vl + hh + sh + ls + dl + gdcd + cn) / 10) / 1.2
        return self.tong_diem
    
    def phan_loai(self):
        if self.tong_diem > 9.0:
            return "XUAT SAC"
        elif 8.0 <= self.tong_diem <= 8.9:
            return "GIOI"
        elif 7.0 <= self.tong_diem <= 7.9:
            return "KHA"
        elif 5.0 <= self.tong_diem <= 6.9:
            return "TB"
        return "YEU"

    def __lt__(self, other):
        if self.tong_diem != other.tong_diem:
            return self.tong_diem > other.tong_diem
        return self.ma < other.ma

if __name__ == "__main__":
    n = int(input())
    ds = []
    
    for i in range(1, n + 1):
        ten = input().strip()
        diem = list(map(float, input().split()))
        ma_hs = f'HS{i:02d}'
        hs = BangDiem(ten, ma_hs)
        hs.diem_trung_binh(*diem)
        ds.append(hs)

    ds.sort() 
    for hs in ds:
        print(f'{hs.ma} {hs.ten} {hs.tong_diem:.1f} {hs.phan_loai()}')