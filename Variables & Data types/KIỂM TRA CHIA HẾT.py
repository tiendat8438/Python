from itertools import combinations
from math import gcd
import sys


# Hàm tính bội số chung nhỏ nhất (LCM)
def lcm(a, b):
    return a * (b // gcd(a, b))

# Sàng Eratosthenes để tìm các số nguyên tố trong đoạn [2, N]
def get_primes(N):
    is_prime = [True] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    return primes

# Đếm số lượng số chia hết cho bất kỳ số nào trong danh sách số nguyên tố bằng Inclusion-Exclusion
def count_divisibles(L, R, primes):
    count = 0
    num_primes = len(primes)

    # Duyệt qua tất cả tập hợp con của các số nguyên tố
    for i in range(1, num_primes + 1):
        for subset in combinations(primes, i):
            lcm_val = 1
            for num in subset:
                lcm_val = lcm(lcm_val, num)
                if lcm_val > R:  # Tránh số quá lớn
                    break

            if lcm_val > R:
                continue

            num_divisible = (R // lcm_val) - ((L - 1) // lcm_val)

            # Áp dụng Inclusion-Exclusion
            if i % 2 == 1:  # Nếu số phần tử lẻ → cộng vào
                count += num_divisible
            else:  # Nếu số phần tử chẵn → trừ đi
                count -= num_divisible

    return count

# Hàm tính số lượng số hợp lệ trong đoạn [L, R]
def count_valid_numbers(L, R, N):
    primes = get_primes(N)  # Lấy danh sách số nguyên tố từ 2 đến N
    total_numbers = R - L + 1
    excluded_count = count_divisibles(L, R, primes)  # Đếm số bị loại
    return total_numbers - excluded_count

data = list(map(int, sys.stdin.read().split()))
i = 0

# Xử lý từng bộ test
while i < len(data):
    if data[i] == -1:  # Điều kiện dừng khi gặp -1
        break
    if i + 2 >= len(data):  # Kiểm tra tránh lỗi truy cập ngoài phạm vi
        break

    L, R, N = data[i], data[i + 1], data[i + 2]
    print(count_valid_numbers(L, R, N))
    
    i += 3  # Di chuyển sang bộ test tiếp theo