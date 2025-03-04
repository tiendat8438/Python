ds = {}
for _ in range(int(input())):
    ma = input()
    ten = input()
    htt = input()
    ds[ma] = (ten, htt)
sorted_ds = sorted(ds.keys())
for key in sorted_ds:
    print(f'{key} {ds[key][0]} {ds[key][1]}')
