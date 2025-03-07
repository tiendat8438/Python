from math import prod

for _ in range(int(input())):
    n = input()
    tong = sum(int(n[i]) for i in range(len(n)) if i % 2 == 0)
    tich = 0
    if all(n[i] == '0' for i in range(len(n)) if i % 2 == 1):
        print(f'{tong} {tich}')
        continue
    tich = prod(int(n[i]) for i in range(len(n)) if i % 2 == 1 and n[i] != '0')
    print(f'{tong} {tich}')