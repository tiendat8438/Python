class NhanVien:
    def __init__(self, ma, ten, luong_co_ban, ngay_cong, phong_ban, he_so_luong):
        self.ma = ma
        self.ten = ten
        self.luong_cb = luong_co_ban
        self.ngay_cong = ngay_cong
        self.phong_ban = phong_ban
        self.he_so_luong = he_so_luong
        self.luong_thang = self.tinh_luong()

    def tinh_luong(self):
        nhom = self.ma[0]  
        nam_ct = int(self.ma[1:3])  

        if nam_ct <= 3:
            he_so = self.he_so_luong[nhom][0]
        elif nam_ct <= 8:
            he_so = self.he_so_luong[nhom][1]
        elif nam_ct <= 15:
            he_so = self.he_so_luong[nhom][2]
        else:
            he_so = self.he_so_luong[nhom][3]

        return int(self.luong_cb * 1000 * self.ngay_cong * he_so)
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.phong_ban} {self.luong_thang}'


if __name__ == "__main__":
    # Bảng hệ số lương
    he_so_luong = {
        'A': [10, 12, 14, 20],
        'B': [10, 11, 13, 16],
        'C': [9, 10, 12, 14],
        'D': [8, 9, 11, 13]
    }

    phong_ban_dict = {}
    for _ in range(int(input())):
        line = input().split(maxsplit=1)
        phong_ban_dict[line[0]] = line[1]  # Mã phòng -> Tên phòng

    ds = []
    for _ in range(int(input())):
        ma = input().strip()
        ten = input().strip()
        luong_cb = int(input().strip())
        ngay_cong = int(input().strip())
        ma_phong = ma[-2:]  
        ten_phong = phong_ban_dict[ma_phong]  # Lấy tên phòng từ dictionary
        ds.append(NhanVien(ma, ten, luong_cb, ngay_cong, ten_phong, he_so_luong))

    for nv in ds:
        print(nv)
