def read_file(filename):
    with open(filename, 'r') as f:
        words = set()
        for line in f:
            words.update(line.strip().lower().split())
    return words

data1 = read_file('DATA1.in')
data2 = read_file('DATA2.in')

dif1 = sorted(data1 - data2)
dif2 = sorted(data2 - data1)
print(' '.join(dif1))
print(' '.join(dif2))