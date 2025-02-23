def sieve(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False
    primes = []
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False

    for i in range(2, n + 1):
        if isPrime[i]:
            primes.append(i)
    return primes

if __name__ == '__main__':
    primes = sieve(100000)
    N, X = map(int, input().split())
    prime_arr = primes[:N]
    res = [X] * (N + 1)
    for i in range(1, N + 1):
        res[i] = res[i - 1] + prime_arr[i - 1]
    print(' '.join(map(str, res)))



