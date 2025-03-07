def solve(n):
    s = str(n)
    if len(s) < 3:
        return "NO"

    dinh = -1  
    for i in range(1, len(s) - 1):
        if s[i] > s[i - 1] and s[i] > s[i + 1]:  
            dinh = i
            break
    if dinh == -1:  
        return "NO"
    for i in range(1, dinh + 1):
        if s[i] <= s[i - 1]:  
            return "NO"
    for i in range(dinh + 1, len(s)):
        if s[i] >= s[i - 1]:  
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    print(solve(n))
    
