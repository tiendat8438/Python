from datetime import datetime

class TramDo:
    def __init__(self, ten_tram):
        self.ten_tram = ten_tram
        self.tong_luong_mua = 0
        self.tong_thoi_gian = 0

    def them_gia_tri(self, start, end, luong_mua):
        fmt = "%H:%M"
        start_time = datetime.strptime(start, fmt)
        end_time = datetime.strptime(end, fmt)
        thoi_gian_mua = (end_time - start_time).total_seconds() / 3600 # Chuyển thành giờ
        self.tong_thoi_gian += thoi_gian_mua
        self.tong_luong_mua += luong_mua

    def luong_mua_trung_binh(self):
        if self.tong_thoi_gian == 0:
            return 0
        return self.tong_luong_mua / self.tong_thoi_gian

    
if __name__ == "__main__":
    danh_sach_tram = {}
    for _ in range(int(input())):
        ten_tram = input()
        start_time = input()
        end_time = input()
        luong_mua = int(input())
        if ten_tram not in danh_sach_tram:
            danh_sach_tram[ten_tram] = TramDo(ten_tram)
        danh_sach_tram[ten_tram].them_gia_tri(start_time, end_time, luong_mua) 
    idx = 1
    ma_tram = {}
    for ten_tram, tram in danh_sach_tram.items():
        if ten_tram not in ma_tram:
            ma_tram[ten_tram] = f"T{idx:02d}"
            idx += 1
        print(f'{ma_tram[ten_tram]} {ten_tram} {tram.luong_mua_trung_binh():.2f}')
    