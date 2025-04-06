def pt(n):
    factors = []
    while n %  2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return factors

with open("INPUT.TXT", 'r', encoding='utf-8') as file:
    m = int(file.readline().strip())
    b = list(map(int, file.readline().strip().split()))

with open("OUTPUT.TXT", 'w', encoding='utf-8') as file:
    for x in b:
        factors = pt(x)
        file.write(f'{len(factors)}\n')
        file.write(' '.join(map(str, factors)) + '\n')