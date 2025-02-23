from collections import defaultdict

bang_gia = {('Xe_con', 5) : 10000,
            ('Xe_con', 7) : 15000,
            ('Xe_tai', 2) : 20000,
            ('Xe_khach', 29) : 50000,
            ('Xe_khach', 45) : 70000
            }

N = int(input())
fees_per_day = defaultdict(int)
for _ in range(N):
    plate, cartype, seats, dir, date = input().split()
    seats = int(seats)
    if dir == 'IN':
        fees_per_day[date] += bang_gia.get((cartype, seats), 0)
for date, totalfee in fees_per_day.items():
    print(f'{date}: {totalfee}')
    
