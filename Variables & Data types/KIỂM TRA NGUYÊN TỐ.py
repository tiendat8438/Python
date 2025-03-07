import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Kiểm tra các số dạng 6k ± 1 từ 5 đến √n
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES" if is_prime(int(s[-4:])) else "NO")