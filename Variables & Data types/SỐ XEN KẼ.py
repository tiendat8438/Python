def solve(s):
    if len(s) % 2 != 1 or s[0] == s[1]:
        return "NO"
    if all(s[i] == s[i + 2] for i in range(len(s) - 1, 2)):
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(solve(s))