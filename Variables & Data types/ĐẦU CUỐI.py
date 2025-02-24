def first_and_last(s):
    return s[:2] == s[-2:]

for _ in range(int(input())):
    s = input()
    print("YES" if first_and_last(s) else "NO")