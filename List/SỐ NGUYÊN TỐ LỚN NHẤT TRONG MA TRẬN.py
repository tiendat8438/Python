def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5)+1):
        if n%i == 0:
            return False
    return True

def find_max_prime(n, m, mat):
    prime_numbers = [mat[i][j] for i in range(n) for j in range(m) if isPrime(mat[i][j])]
    if not prime_numbers:
        return "NOT FOUND", []
    max_prime = max(prime_numbers)
    res = [(i, j) for i in range(n) for j in range(m) if mat[i][j] == max_prime]
    return max_prime, res

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
max_prime, res = find_max_prime(n, m, mat)

if max_prime == "NOT FOUND":
    print("NOT FOUND")
else:
    print(max_prime)
    for i, j in res:
        print(f'Vi tri [{i}][{j}]')