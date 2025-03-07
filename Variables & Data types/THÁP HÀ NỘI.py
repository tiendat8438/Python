def tower(n, a, b, c):
    if n == 1:
        print(f'{a} -> {c}')
        return
    tower(n - 1, a, c, b)
    tower(1, a, b, c)
    tower(n - 1, b, a, c)

if __name__ == "__main__":
    a, b, c = 'A', 'B', 'C'
    n = int(input())
    tower(n, a, b, c)