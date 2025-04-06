data = input().split()
m, v, t = int(data[0]), int(data[1]), int(data[2])
d = str(data[3])
if d == 'A':
    res = (v*t) % m
else:
    res = (m - (v*t % m)) % m
print(res)