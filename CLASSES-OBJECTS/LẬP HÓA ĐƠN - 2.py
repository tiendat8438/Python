from datetime import datetime

class HoaDon:
    def __init__(self, ten, ma, so_phong, chi_phi):
        self.ten = ten
        self.ma = ma
        self.so_phong = so_phong
        self.chi_phi = chi_phi
        self.so_ngay_o = 0
        self.tong_tien = 0

    def thanh_tien(self, start, end):
        fmt = "%d/%m/%Y"
        start_day = datetime.strptime(start, fmt)
        end_day = datetime.strptime(end, fmt)
        self.so_ngay_o = max((end_day - start_day).days + 1, 1)
        # Tính tiền theo loại phòng
        if self.so_phong // 100 == 1:
            gia_phong = 25
        elif self.so_phong // 100 == 2:
            gia_phong = 34
        elif self.so_phong // 100 == 3:
            gia_phong = 50
        else:
            gia_phong = 80

        self.tong_tien = self.so_ngay_o * gia_phong + self.chi_phi

    def __lt__(self, other):
        return self.tong_tien > other.tong_tien  

    def __str__(self):
        return f"{self.ma} {self.ten} {self.so_phong} {self.so_ngay_o} {self.tong_tien}"

if __name__ == "__main__":
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input().strip()
        so_phong = int(input().strip())
        start = input().strip()
        end = input().strip()
        chi_phi = int(input().strip())
        ma = f"KH{i:02d}"

        hoa_don = HoaDon(ten, ma, so_phong, chi_phi)
        hoa_don.thanh_tien(start, end)
        ds.append(hoa_don)

    ds.sort()  # Sắp xếp giảm dần theo tổng tiền

    for kh in ds:
        print(kh)
