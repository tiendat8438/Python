def find_min(s):
    tmp, res = 0, 10**18
    for c in s:
        if c.isdigit():
            tmp = tmp * 10 + int(c)
        else:
            if tmp > 0:
                res = min(res, tmp)
            tmp = 0
    if tmp > 0:
        res = min(res, tmp)
    return res


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        print(find_min(s))
