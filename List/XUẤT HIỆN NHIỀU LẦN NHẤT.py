from collections import Counter

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        counter = Counter(arr)
        if counter.most_common(1)[0][1] > N / 2:
            print(counter.most_common(1)[0][0])
        else:
            print("NO")

