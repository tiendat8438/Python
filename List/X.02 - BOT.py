# Kadane

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    l = r = 0
    start = 0
    sum = 0
    res = -1e9
    for i in range(n):
        sum += A[i]
        if sum < 0:
            sum = 0
            start = i + 1
        if sum > res:
            res = sum
            l, r = start, i
    print(l + 1, r + 1, res)