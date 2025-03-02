class SinhVien:
    def __init__(self, ten, mn1, mn2, mn3, ma):
        self.ten = self.chuan_hoa_ten(ten)
        self.ma = ma
        self.diem_tb = round((mn1 * 3 + mn2 * 3 + mn3 * 2) / 8 + 1e-9, 2)
        self.xep_hang = 0
        
    def chuan_hoa_ten(self, ten):
        return ' '.join(ten.split()).title()

    def __str__(self):
        return f'{self.ma} {self.ten} {self.diem_tb:.2f} {self.xep_hang}'

if __name__ == "__main__":
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input()
        mon1 = float(input())
        mon2 = float(input())
        mon3 = float(input())
        ma = f'SV{i:02d}'
        ds.append(SinhVien(ten, mon1, mon2, mon3, ma))
    sorted_ds = sorted(ds, key=lambda x : (-x.diem_tb, x.ma))
    rank = 1
    for i, sv in enumerate(sorted_ds): # Giúp lấy cả chỉ mục i và sv trg dsds
        if i > 0 and sv.diem_tb == sorted_ds[i - 1].diem_tb:
            sv.xep_hang = sorted_ds[i - 1].xep_hang
        else:
            sv.xep_hang = rank
        rank += 1
    for sv in sorted_ds:
        print(sv)

        