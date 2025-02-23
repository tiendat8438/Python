if __name__ == '__main__':
    m = int(input())
    v = int(input())
    t = int(input())
    d = input()
    distance = v * t
    if d == 'A':
        res = distance % m
    elif d == 'C':
        res = (m - (distance % m)) % m
    print(res)