import heapq

def min_triple_sum(arr):
    if n < 3:
        return float('-inf')
    min1, min2, min3 = heapq.nsmallest(3, arr)
    return min1 + min2 + min3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_triple_sum(arr))