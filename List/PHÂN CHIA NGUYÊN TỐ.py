def isPrime(n):
    if n<2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(A, n):
    B = list(dict.fromkeys(A))
    m = len(B)
    total = sum(B)
    left_sum = 0 # Tổng bên trái
    for i in range(m - 1):
        left_sum += B[i] 
        right_sum = total - left_sum  # Tổng bên phải
        if isPrime(left_sum) and isPrime(right_sum):
            return i
    return 'NOT FOUND'

n = int(input())
A = list(map(int, input().split()))
print(solve(A, n))
