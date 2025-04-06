import random

def read_input(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    expressions = [line.strip() for line in lines]
    return n, expressions

def solve(n, expressions):
    a = random.randint(-10, 10)
    b = random.randint(-5, 5)
    c = random.randint(0, 10)

    res = []
    for expr in expressions:
        try:
            val = eval(expr, {'a' : a, 'b' : b, 'c' : c})
            res.append(val)
        except:
            res.append(0)
    avg = sum(res) / n
    avg = round(avg, 6)

    min_range = avg * 0.8
    max_range = avg * 1.2

    valid_in = [i + 1 for i in range(n) if min_range <= res[i] <= max_range]
    return a, b, c, avg, len(valid_in), valid_in

def write_ouput(file, a, b, c, avg, cnt, valid_in):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(f'a,b,c: {a} {b} {c}\n')
        f.write(f'Average: {avg}\n')
        f.write(f'Total results in range: {cnt}\n')
        if cnt > 0:
            f.write('Winners: ' + ' '.join(map(str, valid_in)))

input_data = "INPUT.TXT"
output_data = 'OUTPUT.TXT'
n, expressions = read_input(input_data)
a, b, c, avg, cnt, valid_in = solve(n, expressions)
write_ouput(output_data, a, b, c, avg, cnt, valid_in)

