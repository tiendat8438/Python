def rev(n):
    n = str(n)
    return int(n[::-1])

for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
        continue
    t = 1000
    sum = 0
    while t > 0:
        if sum % 7 == 0 and sum != 0:
            print(sum)
            break
        sum = n + rev(n)
        n = sum
    else:
        print(-1)