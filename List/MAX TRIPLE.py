import heapq

def max_triple_sum(arr):
    if n < 3:
        return float('-inf')
    max1, max2, max3 = heapq.nlargest(3, arr)
    return max1 + max2 + max3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_triple_sum(arr))