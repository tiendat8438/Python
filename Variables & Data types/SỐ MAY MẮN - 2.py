for _ in range(int(input())):
    s = input()
    print("YES" if all(s[i] == '4' or s[i] == '7' for i in range(len(s))) else "NO")