MOD = 1000
""" Sử dụng công thức truy hồi để tính toán (3 + sqrt(5))^n và (3 - sqrt(5))^n cùng lúc, 
sau đó sử dụng kết quả này để tìm ra phần nguyên của (3 + sqrt(5))^n."""
"""Chúng ta có thể sử dụng công thức truy hồi để tính toán (3 + sqrt(5))^n và (3 - sqrt(5))^n:
Đặt a_n = (3 + sqrt(5))^n + (3 - sqrt(5))^n.
Khi đó, a_n là một số nguyên vì (3 - sqrt(5))^n là một số rất nhỏ và sẽ không ảnh hưởng đến phần nguyên của (3 + sqrt(5))^n.
Sau đó, chúng ta có thể tính a_n bằng công thức truy hồi:
a_0 = 2
a_1 = 6
a_n = 6 * a_{n-1} - 4 * a_{n-2}
Cuối cùng, phần nguyên của (3 + sqrt(5))^n sẽ là a_n - 1 (vì (3 - sqrt(5))^n rất nhỏ)."""

# sử dụng phương pháp lũy thừa nhanh (fast exponentiation) 
def matrix_mult(a, b):
    return [[(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
             (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD],
            [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
             (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD]]

def matrix_pow(mat, power):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        power = power // 2
    return result

def get_three_digits(n):
    if n == 0:
        return "001"
    # Transformation matrix for the recurrence a_n = 6*a_{n-1} - 4*a_{n-2}
    mat = [[6, -4], [1, 0]]
    mat_pow = matrix_pow(mat, n - 1)
    # a_n = mat_pow[0][0] * a_1 + mat_pow[0][1] * a_0
    a_n = (mat_pow[0][0] * 6 + mat_pow[0][1] * 2) % MOD
    result = (a_n - 1) % MOD
    return f"{result:03d}"

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    ans = get_three_digits(n)
    print(f'Case #{t}: {ans}')