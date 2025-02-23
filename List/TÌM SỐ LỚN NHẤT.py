def find_max(s):
    tmp, res = 0, 0
    for c in s:
        if c.isdigit():
            tmp = tmp*10 + int(c)
        else:
            res = max(res, tmp)
            tmp = 0
    res = max(res, tmp)
    return res

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        print(find_max(s))