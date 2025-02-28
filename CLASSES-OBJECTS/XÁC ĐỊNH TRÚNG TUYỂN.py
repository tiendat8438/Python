class XetTuyen:
    def __init__(self, ten, ma_xet, ma_GV):
        self.ten = ten
        self.ma_xet = ma_xet
        self.ma_GV = ma_GV
        self.tong_diem = 0
    
    def xac_dinh(self):
        chuyen_mon = self.ma_xet[0]
        mon = ''
        if chuyen_mon == 'A':
            mon += 'TOAN'
        elif chuyen_mon == 'B':
            mon += 'LY'
        else:
            mon += 'HOA'
        return mon 

    def tinh_diem(self, tin_hoc, mon_thi):
        uu_tien = self.ma_xet[1]
        if uu_tien == '1':
            self.tong_diem += 2*tin_hoc + mon_thi + 2.0
        elif uu_tien == '2':
            self.tong_diem += 2*tin_hoc + mon_thi + 1.5
        elif uu_tien == '3':
            self.tong_diem += 2*tin_hoc + mon_thi + 1.0
        else:
            self.tong_diem += 2*tin_hoc + mon_thi + 0.0

    def phan_loai(self):
        if self.tong_diem < 18:
            return "LOAI"
        else:
            return "TRUNG TUYEN"
    
    def __lt__(self, other):
        return self.tong_diem > other.tong_diem
    
    def __str__(self):
        return f'{self.ma_GV} {self.ten} {self.xac_dinh()} {self.tong_diem:.1f} {self.phan_loai()}'
    
if __name__ == "__main__":
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input()
        ma_xet = input()
        tin_hoc = float(input())
        mon_thi = float(input())
        ma_GV = f'GV{i:02d}'
        xet_tuyen = XetTuyen(ten, ma_xet, ma_GV)
        xet_tuyen.tinh_diem(tin_hoc, mon_thi)
        ds.append(xet_tuyen)
    ds.sort()
    for gv in ds:
        print(gv)

