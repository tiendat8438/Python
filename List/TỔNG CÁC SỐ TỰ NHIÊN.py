def find(n, max_num, cur, res):
    if n == 0:
        res.append(cur)
        return
    for i in range(1, min(n, max_num) + 1):
        find(n - i, i, cur + [i], res)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = []
        find(n, n, [], res)
        print(len(res))
        print(" ".join(f"({' '.join(map(str, x))})" for x in res[::-1]))