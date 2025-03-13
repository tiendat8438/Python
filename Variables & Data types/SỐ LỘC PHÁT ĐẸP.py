def check(n):
    if any(n[i] not in ['6', '8'] for i in range(len(n))):
        return 'NO'
    i = 0
    while i < len(n):
        if i + 3 <= len(n) and n[i:i + 3] == '688':
            i += 3
        elif i + 2 <= len(n) and n[i:i + 2] == '68': 
            i += 2
        elif n[i] == '6':
            i += 1
        else:
            return "NO"
    return "YES"

print(check(input()))