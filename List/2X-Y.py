from math import gcd

def solve(A, n, k):
    # Nếu k đã có sẵn trong mảng, trả về YES ngay
    if k in A:
        return 'YES'
    # Tính GCD của tất cả hiệu giữa các phần tử trong mảng
    gcd_val = 0
    for i in range(1, n):
        gcd_val = gcd(gcd_val, A[i] - A[0])
    # Kiểm tra xem k có thể tạo từ arr[0] + m * gcd_val không
    if (k - A[0]) % gcd_val == 0:
        return "YES"
    return "NO"

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(A, n, k))
