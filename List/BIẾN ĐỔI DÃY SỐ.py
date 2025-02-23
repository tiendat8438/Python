def count(A):
    steps = 0
    while True:
        if A[0] == A[1] == A[2] == A[3]:
            return steps
        newA = [abs(A[0] - A[1]),
                abs(A[1] - A[2]),
                abs(A[2] - A[3]),
                abs(A[3] - A[0])]
        A = newA
        steps += 1



if __name__ == '__main__':
    while True:
        A = list(map(int, input().split()))
        if A == [0, 0, 0, 0]:
            break
        print(count(A))