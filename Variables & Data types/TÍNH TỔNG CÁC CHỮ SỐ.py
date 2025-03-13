for _ in range(int(input())):
    s = input()
    A = sorted([c for c in s if c.isalpha()])
    tong = sum(int(c) for c in s if c.isdigit())
    print(''.join(A) + str(tong))