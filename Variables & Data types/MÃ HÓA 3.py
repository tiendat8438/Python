def char_to_val(c):
    return ord(c) - ord('A')

def val_to_char(v):
    return chr((v % 26) + ord('A'))

def rotate(s):
    shift = sum(char_to_val(c) for c in s)
    return ''.join(val_to_char(char_to_val(c) + shift) for c in s)

def merge(s1, s2):
    return ''.join(val_to_char(char_to_val(c1) + char_to_val(c2)) for c1,c2 in zip(s1, s2))

def solve(s):
    mid = len(s) // 2
    part1, part2 = s[:mid], s[mid:]
    rotated1, rotated2 = rotate(part1), rotate(part2)
    return merge(rotated1, rotated2)

for _ in range(int(input())):
    s = input()
    print(solve(s))