def add_big_nums(a, b):
    if len(a) < len(b):
        a, b = b, a
    a = list(a)
    b = list(b)
    carry = 0
    res = []
    while a:
        digit_a = int(a.pop())
        digit_b = int(b.pop()) if b else 0
        sum = digit_a + digit_b + carry
        carry = sum // 10
        res.append(str(sum % 10))
    if carry:
        res.append(str(carry))
    ans = ''.join(res[::-1]).lstrip('0')
    return ans if ans else '0'

a = input()
b = input()
print(add_big_nums(a, b))
