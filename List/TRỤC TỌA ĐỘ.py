T = int(input())
for _ in range(T):
    n = int(input())
    A = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : x[1])
    cnt, last_end = 0, -1
    for x1, x2 in A:
        if x1 >= last_end:
            cnt += 1
            last_end = x2
    print(cnt)

    