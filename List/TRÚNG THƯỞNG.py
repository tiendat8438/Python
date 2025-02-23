from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    mylist = []
    for _ in range(N):
        stt = int(input())
        mylist.append(stt)
    counter = Counter(mylist)
    max_freq = max(counter.values())
    stt = [num for num, freq in counter.items() if freq == max_freq]
    print(min(stt))