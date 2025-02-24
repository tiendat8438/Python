def solve(s):
    s2 = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(solve(s))
    