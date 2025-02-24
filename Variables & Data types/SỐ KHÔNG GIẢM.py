def check(s):
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))

for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else 'NO')
