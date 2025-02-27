class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem_chuyen_can = 10  # Điểm chuyên cần tối đa

    def tinh_diem_chuyen_can(self, diem_danh):
        diem_tru = diem_danh.count('v') * 2 + diem_danh.count('m')
        self.diem_chuyen_can = max(0, 10 - diem_tru)  # Không để điểm âm

    def __str__(self):
        ghi_chu = " KDDK" if self.diem_chuyen_can == 0 else ""
        return f"{self.ma} {self.ten} {self.lop} {self.diem_chuyen_can}{ghi_chu}"

if __name__ == "__main__":
    n = int(input())
    danh_sach_sv = {}
    for _ in range(n):
        ma = input()
        ten = input()
        lop = input()
        danh_sach_sv[ma] = SinhVien(ma, ten, lop)

    # Nhập dữ liệu điểm danh và tính điểm
    for _ in range(n):
        ma, diem_danh = input().split()
        if ma in danh_sach_sv:
            danh_sach_sv[ma].tinh_diem_chuyen_can(diem_danh)

    # In kết quả
    for sv in danh_sach_sv.values():
        print(sv)
