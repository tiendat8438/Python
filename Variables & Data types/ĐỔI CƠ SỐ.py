def solve(N, b):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Chứa các ký tự từ 0-9 và A-Z
    result = ""
    while N > 0:
        result = chars[N % b] + result  
        N //= b  
    return result if result else "0"  # Trả về "0" nếu N = 0


for _ in range(int(input())):
    n, b = map(int, input().split())
    print(solve(n, b))