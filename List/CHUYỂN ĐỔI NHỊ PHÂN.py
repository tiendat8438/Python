def convert(x, b):
    decimal_val = int(x, 2)
    if b == 2:
        return x
    elif b == 4:
        while len(x) % 2 != 0: 
            x = '0' + x
        mapping = {"00": "0", "01": "1", "10": "2", "11": "3"}
        return ''.join(mapping[x[i:i+2]] for i in range(0, len(x), 2))
    elif b == 8:
        return format(decimal_val, 'o')
    elif b == 16:
        return format(decimal_val, 'X')

if __name__ == '__main__':
    with open("DATA.in", 'r') as file:
        lines = file.readlines()
    T = int(lines[0])
    idx = 1
    for _ in range(T):
        b = int(lines[idx])
        x = lines[idx + 1]
        idx += 2
        print(convert(x, b))

