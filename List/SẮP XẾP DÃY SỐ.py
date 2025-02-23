T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(A.index(max(A)), m)
    neg = [num for num in A if num < 0]
    non_neg = [num for num in A if num >= 0]
    print(*neg, *non_neg)
    
    