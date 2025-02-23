fib = [0] * 93
fib[1] = 1
fib[2] = 1
for i in range(3, 93):
    fib[i] = fib[i - 1] + fib[i - 2]
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(*fib[a:b + 1])
