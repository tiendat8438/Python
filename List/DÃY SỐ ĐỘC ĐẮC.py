def is_doc_dac(A, n):
    freq = {}
    unique_count = 0
    def add(x):
        nonlocal unique_count
        if x in freq:
            if freq[x] == 1:
                unique_count -= 1
            freq[x] += 1
        else:
            freq[x] = 1
            unique_count += 1
    
    def remove(x):
        nonlocal unique_count
        if x in freq:
            if freq[x] == 1:
                unique_count -= 1
                del freq[x]
        else:
            freq[x] -= 1
            if freq[x] == 1:
                unique_count += 1

    for L in range(1, n):
        freq.clear()
        unique_count = 0

        for i in range(L):
            add(A[i])
        if unique_count == 0:
            return "NO"
        for i in range(L, n):
            add(A[i])
            remove(A[i - L])    
            if unique_count == 0:
                return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    print(is_doc_dac(A, n))