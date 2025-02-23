from datetime import datetime

class CaThi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma = ma
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.thoi_gian = datetime.strptime(ngay + " " + gio, "%d/%m/%Y %H:%M")

    def __lt__(self, other):
        if self.thoi_gian != other.thoi_gian:
            return self.thoi_gian < other.thoi_gian
        return self.ma < other.ma
    
    def __str__(self):
        return f'{self.ma} {self.ngay} {self.gio} {self.phong}'
    
with open("CATHI.in", 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    ds = []
    for i in range(1, n + 1):
        ngay = file.readline().strip()
        gio = file.readline().strip()
        phong = file.readline().strip()
        ma = f'C{i:03}'
        ds.append(CaThi(ma, ngay, gio, phong))

ds.sort()

for ca in ds:
    print(ca)