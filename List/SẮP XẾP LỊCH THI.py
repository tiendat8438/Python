from datetime import datetime

mon_thi = {}
with open("MONTHI.in", 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    for _ in range(n):
        ma_mon = file.readline().strip()
        ten_mon = file.readline().strip()
        hinh_thuc = file.readline().strip()
        mon_thi[ma_mon] = ten_mon

ca_thi = {}
with open("CATHI.in", 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    for i in range(1,n+1):
        ngay = file.readline().strip()
        gio = file.readline().strip()
        ma_ca = f'C{i:03}'
        phong = file.readline().strip()
        ca_thi[ma_ca] = (ngay, gio, phong)

lich_thi = []
with open("LICHTHI.in", 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    for _ in range(n):
        ma_ca, ma_mon, nhom, so_sv = file.readline().strip().split()
        ngay, gio, phong = ca_thi[ma_ca]
        ten_mon = mon_thi[ma_mon]
        thoi_gian = datetime.strptime(ngay + " " + gio, '%d/%m/%Y %H:%M')
        lich_thi.append((thoi_gian, ma_ca, ngay, gio, phong, ten_mon, nhom, int(so_sv)))

lich_thi.sort()

for _, ma_ca, ngay, gio, phong, ten_mon, nhom, so_sv in lich_thi:
    print(ngay, gio, phong, ten_mon, nhom, so_sv)
