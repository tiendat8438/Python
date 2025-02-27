class HoaDon:
    def __init__(self, ten, ma, old, new):
        self.ten = ten
        self.ma = ma
        self.so_nuoc_da_dung = new - old
        self.tinh_tien()

    def tinh_tien(self):
        if self.so_nuoc_da_dung <= 50:
            tien_nuoc = self.so_nuoc_da_dung * 100
            phu_phi = tien_nuoc * 0.02
        elif self.so_nuoc_da_dung <= 100:
            tien_nuoc = 50 * 100 + (self.so_nuoc_da_dung - 50) * 150
            phu_phi = tien_nuoc * 0.03
        else:
            tien_nuoc = 50 * 100 + 50 * 150 + (self.so_nuoc_da_dung - 100) * 200
            phu_phi = tien_nuoc * 0.05

        self.tong_tien = round(tien_nuoc + phu_phi)

    def __lt__(self, other):
        return (self.tong_tien, other.ma) > (other.tong_tien, self.ma)  # Sắp xếp theo tổng tiền giảm dần, mã khách hàng tăng dần

if __name__ == "__main__":
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input().strip()
        old_stat = int(input())
        new_stat = int(input())
        ma = f'KH{i:02d}'
        ds.append(HoaDon(ten, ma, old_stat, new_stat))

    ds.sort()  # Dùng phương thức __lt__

    for kh in ds:
        print(f'{kh.ma} {kh.ten} {kh.tong_tien}')
