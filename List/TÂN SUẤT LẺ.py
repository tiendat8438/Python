from collections import Counter

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    counter = Counter(A)
    for key, val in counter.items():
        if (counter[key] % 2 == 1):
            print(key)
            break
            

        
