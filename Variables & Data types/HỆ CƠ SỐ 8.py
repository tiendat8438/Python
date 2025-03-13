def solve(n):
    decimal_val = int(n, 2)
    return format(decimal_val, 'o')

print(solve(input()))