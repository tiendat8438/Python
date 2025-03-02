from datetime import datetime

class Subject:
    def __init__(self, ma_mon, ten):
        self.ma_mon = ma_mon
        self.ten = ten

class CaThi:
    def __init__(self, ma_mon, ma_ca_thi, nhom, mon_hoc_dict, date):
        self.ma_mon = ma_mon
        self.ma_ca_thi = ma_ca_thi
        self.nhom = nhom
        self.date = datetime.strptime(date, "%d/%m/%Y %H:%M")
        self.ten_mon_hoc = mon_hoc_dict[ma_mon]
    def __lt__(self, other):
        if self.date != other.date:
            return self.date < other.date
        return self.ma_mon < other.ma_mon
    def __str__(self):
        return f'{self.ma_ca_thi} {self.ma_mon} {self.ten_mon_hoc} {self.date.strftime("%d/%m/%Y %H:%M")} {self.nhom}'        
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    mon_hoc_dict = {}
    for _ in range(n):
        ma_mon = input()
        ten = input()
        mon_hoc_dict[ma_mon] = ten
    ds = []
    for i in range(1, m + 1):
        data = input().split()
        ma_mon, ngay, gio, nhom = data
        date = ngay + " " + gio
        ma_ca_thi = f'T{i:03d}'
        ds.append(CaThi(ma_mon, ma_ca_thi, nhom, mon_hoc_dict, date))
    ds.sort()
    for ca in ds:
        print(ca)

