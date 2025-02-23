if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        A = [int(input()) for _ in range(N)]
        if all(A[i] == A[i + 1] for i in range(N - 1)):
            print("BANG NHAU")
        else:
            print(f'{min(A)} {max(A)}')