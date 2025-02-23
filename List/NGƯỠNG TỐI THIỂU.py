from collections import Counter

def limit(A, k):
    counter = Counter(A)
    res = [(key, val) for key, val in counter.items() if val >= k]
    if not res:
        return "NOT FOUND"
    sorted_list = sorted(res, key=lambda x : x[0])
    return sorted_list
    

s = input() 
k = int(input())
A = [s[i:i+2] for i in range(0, len(s) - 1, 2)]
res = limit(A, k)
if res == 'NOT FOUND':
    print(res)
else:
    for key, val in res:
        print(f'{key} {val}')
