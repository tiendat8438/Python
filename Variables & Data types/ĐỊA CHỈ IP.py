def solve(s):
    x = s.split('.')
    if len(x) != 4:
        return "NO"
    for c in x:
        if not c.isdigit():
            return 'NO'
        num = int(c)
        if num < 0 or num > 255:
            return 'NO'
        if len(c) > 1 and c[0] == '0':
            return 'NO'
    return "YES"

for _ in range(int(input())):
    s = input()
    print(solve(s))

