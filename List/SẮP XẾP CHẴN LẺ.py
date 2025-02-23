if __name__ == '__main__':
    while True:
        line = input().strip()
        if line: # bỏ qua các dòng trống
            N = int(line)
            break
    A = [] # các phần tử nằm rải rác từng dòng
    while len(A) < N:
        line = input().strip()
        if line:
            A.extend(map(int, line.split()))
    odd_idx, even_idx = 0, 0
    evenA = sorted([num for num in A if num % 2 == 0])
    oddA = sorted([num for num in A if num % 2 == 1], reverse=True)
    res = []
    for i in range(N):
        if A[i] % 2 == 0:
            res.append(evenA[even_idx])
            even_idx += 1
        else:
            res.append(oddA[odd_idx])
            odd_idx += 1
    print(*res)



