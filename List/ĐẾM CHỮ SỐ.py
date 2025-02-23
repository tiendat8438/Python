def f(x, n): # Số lần xuất hiện của x trong phạm vi 1 đến n theo các bậc đơn vị(chục, trăm, ...)
    res = 0
    for i in range(0, 10):
        m = 10**i  # Tính giá trị của bậc i
        if m > n: break
        a = n // m  # Lấy phần nguyên để xử lý phần trước của số tại i
        b = n % m   # Lấy phần dư để xử lý phần sau của số tại i
        z = a % 10  # Lấy chữ số tại vị trí i trong số n
        if z > x: res += ((a // 10) + 1) * m    # Chữ số tại vị trí này lớn hơn x thì chữ số xuất hiện ở bậc này sẽ xuất hiện trong 
        # tất cả các số từ 1 đến n và có số lần xuất hiện
        elif z == x: res += (a // 10) * m + (b + 1)
        else: res += (a // 10) * m
        if x == 0: res -= m     # Không đếm các só bắt đầu bằng số 0
    return res

# Trả về số lần xuất hiện của chữ số d trong [low, high]
def digitsCount(d, low, high):
    return f(d, high) - f(d, low - 1) 

for t in range(int(input())):
    a, b = map(int, input().split())
    for i in range(0, 10): print(digitsCount(i, a, b), end=' ')
    print()