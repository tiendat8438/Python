s = input()
A = [s[i:i+2] for i in range(0, len(s) - 2, 2)]
B = list(dict.fromkeys(A))
print(*B)
