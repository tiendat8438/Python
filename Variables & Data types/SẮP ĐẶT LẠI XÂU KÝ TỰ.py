def solve(s1, s2):
    if len(s1) != len(s2):
        return False
    char_count = {}
    for c in s1:
        char_count[c] = char_count.get(c, 0) + 1
    for c in s2:
        if c not in char_count or char_count[c] == 0:
            return False
        char_count[c] -= 1
    return True

for t in range(1, int(input()) + 1):
    s1, s2 = input(), input()
    if solve(s1, s2):
        print(f'Test {t}: YES')
    else:
        print(f'Test {t}: NO')
    
    