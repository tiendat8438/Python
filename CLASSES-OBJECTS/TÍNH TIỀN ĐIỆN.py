class KhachHang:
    def __init__(self, ten, type, ma, dau, cuoi, dinh_muc):
        self.ten = self.chuan_hoa_ten(ten)
        self.type = type
        self.ma = ma
        self.dau = dau
        self.cuoi = cuoi
        self.dinh_muc = dinh_muc
        self.tien_trong_dm = 0
        self.tien_vuot_dm = 0
        self.vat = 0
        self.tong_tien = self.tinh_tien()

    def chuan_hoa_ten(self, ten):
        return ' '.join(ten.split()).title()

    def tinh_tien(self):
        so_dien = self.cuoi - self.dau
        dm = self.dinh_muc[self.type]

        if so_dien <= dm:
            self.tien_trong_dm = so_dien * 450
            self.tien_vuot_dm = 0
        else:
            self.tien_trong_dm = dm * 450
            self.tien_vuot_dm = (so_dien - dm) * 1000
        
        self.vat = self.tien_vuot_dm * 5 // 100  
        return int(self.tien_trong_dm + self.tien_vuot_dm + self.vat)

    def __lt__(self, other):
        return self.tong_tien > other.tong_tien  

    def __str__(self):
        return f'{self.ma} {self.ten} {self.tien_trong_dm} {self.tien_vuot_dm} {self.vat} {self.tong_tien}'


if __name__ == "__main__":
    bang_dinh_muc = {'A': 100, 'B': 500, 'C': 200}
    ds = []

    for i in range(1, int(input()) + 1): 
        ten = input().strip()
        line = input().split()
        type = line[0]
        dau = int(line[1])
        cuoi = int(line[2])
        ma = f'KH{i:02d}'
        ds.append(KhachHang(ten, type, ma, dau, cuoi, bang_dinh_muc))

    ds.sort()
    for kh in ds:
        print(kh)