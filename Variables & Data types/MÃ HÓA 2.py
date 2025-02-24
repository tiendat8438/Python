if __name__ == "__main__":
    while True:
        data = input().split()
        k = int(data[0])
        if k == 0: break
        P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
        s = data[1]
        res = ''
        for c in s:
            new_c = P[(P.index(c) + k) % 28]
            res += new_c
        print(res[::-1])