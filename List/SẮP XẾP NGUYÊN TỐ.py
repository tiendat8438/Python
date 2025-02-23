def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n>1

n = int(input())
A = list(map(int, input().split()))
primes = sorted([num for num in A if isPrime(num)])
prime_idx = 0
res = []
for i in range(n):
    if isPrime(A[i]):
        res.append(primes[prime_idx])
        prime_idx += 1
    else:
        res.append(A[i])
print(*res)

