from datetime import datetime

class Player:
    def __init__(self, ten, ma):
        self.ten = ten
        self.ma = ma
        self.tong_thoi_gian = 0  

    def thoi_gian_choi_game(self, start, end):
        fmt = '%H:%M'
        start_time = datetime.strptime(start, fmt)
        end_time = datetime.strptime(end, fmt)
        self.tong_thoi_gian += (end_time - start_time).total_seconds()

    def __lt__(self, other):
        return self.tong_thoi_gian > other.tong_thoi_gian  

if __name__ == "__main__":
    ds = []
    for _ in range(int(input())):
        ma = input().strip()
        ten = input().strip()
        start = input().strip()
        end = input().strip()
        
        nguoi_choi = Player(ten, ma)
        nguoi_choi.thoi_gian_choi_game(start, end)
        ds.append(nguoi_choi)
    ds.sort() 
    for nguoi_choi in ds:
        gio = int(nguoi_choi.tong_thoi_gian // 3600)
        phut = int((nguoi_choi.tong_thoi_gian % 3600) // 60)
        print(f'{nguoi_choi.ma} {nguoi_choi.ten} {gio} gio {phut} phut')
