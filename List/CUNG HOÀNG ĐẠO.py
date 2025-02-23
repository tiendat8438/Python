def solve(d, m):
    signs =  [('Bach Duong', 21, 3, 19, 4),
              ('Kim Nguu', 20, 4, 20, 5),
              ('Song Tu', 21, 5, 20, 6),
              ('Cu Giai', 21, 6, 22, 7),
              ('Su Tu', 23, 7, 22, 8),
              ('Xu Nu', 23, 8, 22, 9),
              ('Thien Binh', 23, 9, 22, 10),
              ('Thien Yet', 23, 10, 22, 11),
              ('Nhan Ma', 23, 11, 21, 12),
              ('Ma Ket', 22, 12, 19, 1),
              ('Bao Binh', 20, 1, 18, 2),
              ('Song Ngu', 19, 2, 20, 3)]
    for sign, start_day, start_month, end_day, end_month in signs:
        if(m == start_month and d >= start_day) or (m == end_month and d <= end_day):
            return sign


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        d, m = map(int, input().split())
        print(solve(d, m))
