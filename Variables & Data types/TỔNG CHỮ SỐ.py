s = input()
cnt, sum = 0, 0
while len(s) > 1:
    for i in s:
        sum += ord(i) - ord('0')
    cnt += 1
    s = str(sum)
print(cnt)