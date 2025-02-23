# def tong(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n = n // 10
#     return sum

def tich(n):
    res = 1
    while n > 0:
        res *= n % 10
        n = n // 10
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = [(num, tich(num)) for num in A]
    sorted_list = sorted(B, key=lambda x: (x[1], x[0]))
    for num in sorted_list:
        print(num[0], end = ' ')
    print()



