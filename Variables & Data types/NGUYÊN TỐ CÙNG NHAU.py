from math import gcd

n, k = map(int, input().split())
res = []
start = 10**(k-1)
end = 10**k
result = []
    
for num in range(start, end):
    if gcd(num, n) == 1:
        result.append(num)
for i in range(0, len(result), 10):
    print(" ".join(map(str, result[i:i+10])))