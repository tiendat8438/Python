def solve(n):
    s = str(n)
    if len(set(s)) > 2:
        return "NO"
    for i in range(len(s) - 2):
        if s[i] != s[i + 2]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    print(solve(n))