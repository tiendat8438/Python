from datetime import datetime

class TheLoai:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class Phim:
    def __init__(self, ma_the_loai, date, ten, so_tap, ma_phim, the_loai_dict):
        self.ten = ten
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.ma_phim = ma_phim
        self.ma_the_loai = ma_the_loai
        self.ten_the_loai = the_loai_dict[ma_the_loai]
        self.so_tap = int(so_tap)

    def __lt__(self, other):
        if self.date != other.date:
            return self.date < other.date  # Ngày tăng dần
        if self.ten != other.ten:
            return self.ten < other.ten  # Tên từ điển
        return self.so_tap > other.so_tap  # Số tập giảm dần

    def __str__(self):
        return f'{self.ma_phim} {self.ten_the_loai} {self.date.strftime("%d/%m/%Y")} {self.ten} {self.so_tap}'

if __name__ == "__main__":
    n, m = map(int, input().split())
    the_loai_dict = {}

    # Nhập danh sách thể loại
    for i in range(1, n + 1):
        the_loai = input().strip()
        ma_the_loai = f'TL{i:03d}'
        the_loai_dict[ma_the_loai] = the_loai

    phim_list = []

    # Nhập danh sách phim
    for i in range(1, m + 1):
        ma_tl = input()
        ngay = input()
        ten = input()
        so_tap = int(input())

        ma_phim = f'P{i:03d}'
        phim_list.append(Phim(ma_tl, ngay, ten, so_tap, ma_phim, the_loai_dict))

    # Sắp xếp danh sách phim theo yêu cầu
    phim_list.sort()

    # In kết quả
    for phim in phim_list:
        print(phim)
