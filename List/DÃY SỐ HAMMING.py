N = 10**18

def is_hamming(N):
    for p in [2, 3, 5]:
        while N % p == 0:
            N //= p
    return N == 1

def hamming(limit):
    hamming_list = [1]
    idx = 0
    while True:
        cur = hamming_list[idx]
        for p in [2, 3, 5]:
            tmp = cur * p
            if tmp > N:
                return hamming_list
            if tmp not in hamming_list:
                hamming_list.append(tmp)
        idx += 1
        hamming_list.sort()
    

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        hamming_nums = hamming(N)
        if is_hamming(n):
            print(hamming_nums.index(n) + 1)
        else:
            print("Not in sequence")
        
