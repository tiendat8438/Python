def check(n):
    return "YES" if n[0] == n[-1] else "NO"

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = input().strip()
        print(check(n))
