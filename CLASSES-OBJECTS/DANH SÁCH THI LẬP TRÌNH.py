class Team:
    def __init__(self, ma_team, ten_team, ten_truong):
        self.ma_team = ma_team
        self.ten_team = ten_team
        self.ten_truong = ten_truong
    
class ThiSinh:
    def __init__(self, ten, ma_TS, ma_team, ten_team_dict):
        self.ten = ten
        self.ma_TS = ma_TS
        self.ma_team = ma_team
        self.ten_team = ten_team_dict[ma_team]
    def __lt__(self, other):
        return self.ten < other.ten
    def __str__(self):
        return f'{self.ma_TS} {self.ten} {' '.join(self.ten_team)}'

if __name__ == "__main__":
    ten_team_dict = {}
    for i in range(1, int(input()) + 1):
        ten_team = input()
        ten_truong = input()
        ma_team = f'Team{i:02d}'
        ten_team_dict[ma_team] = (ten_team, ten_truong)
    ds = []
    for i in range(1, int(input()) + 1):
        ten = input()
        ma_team = input()
        ma_TS = f'C{i:03d}'
        ds.append(ThiSinh(ten, ma_TS, ma_team, ten_team_dict))
    ds.sort()
    for ts in ds:
        print(ts)

