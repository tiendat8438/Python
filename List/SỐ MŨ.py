import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  # Không tồn tại nghịch đảo
    return x % m

def baby_step_giant_step(a, b, M):
    if b == 1:  # Trường hợp đặc biệt a^0 ≡ 1 (mod M)
        return 0
    
    m = int(math.isqrt(M)) + 1
    baby_steps = {}

    # Baby-step: Lưu trữ a^j (mod M)
    current = 1
    for j in range(m):
        if current not in baby_steps:
            baby_steps[current] = j
        current = (current * a) % M

    # Giant-step: Tính a^(-m) mod M
    c = modinv(a, M)
    if c is None:
        return -1
    c = pow(c, m, M)

    # Duyệt theo từng bước lớn
    current = b
    for i in range(m):
        if current in baby_steps:
            return i * m + baby_steps[current]
        current = (current * c) % M

    return -1

def main():
    T = int(input().strip())
    for _ in range(T):
        a, b, M = map(int, input().split())
        print(baby_step_giant_step(a, b, M))

if __name__ == "__main__":
    main()
