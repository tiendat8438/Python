for _ in range(int(input())):
    s = input()
    print("YES" if all(s[i] in ['0', '1', '2'] for i in range(len(s))) else "NO")