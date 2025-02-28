from datetime import datetime

class BXH:
    def __init__(self, ten, ma, donvi):
        self.ten = ten
        self.donvi = donvi
        self.ma = ma
        self.tong_thoi_gian = 0
        self.van_toc_trung_binh = 0
        self.quang_duong = 120
        self.start_time = datetime.strptime("6:00", "%H:%M")

    def thanh_tich(self, end_time):
        end_time = datetime.strptime(end_time, "%H:%M")
        self.tong_thoi_gian = (end_time - self.start_time).total_seconds() / 3600
        self.van_toc_trung_binh = round(self.quang_duong / self.tong_thoi_gian)

    def __lt__(self, other):
        return self.tong_thoi_gian < other.tong_thoi_gian
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.donvi} {self.van_toc_trung_binh} Km/h'

def generate_code(full_name, province):
    province_code = ''.join(word[0].upper() for word in province.split())
    name_code = ''.join(word[0].upper() for word in full_name.split())    
    return province_code + name_code


if __name__ == "__main__":
    ds = []
    for _ in range(int(input())):
        ten = input().strip()
        don_vi = input().strip()
        end_time = input().strip()
        ma = generate_code(ten, don_vi)
        bxh = BXH(ten, ma, don_vi)
        bxh.thanh_tich(end_time)
        ds.append(bxh)
    
    ds.sort()
    
    for thi_sinh in ds:
        print(thi_sinh)
