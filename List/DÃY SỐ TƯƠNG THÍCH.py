from math import ceil
n = int(input())
A = sorted(list(map(int, input().split())))
cnt = 1
while (cnt < A[0]):
    B = []
    ans = A[0] // cnt
    for i in range(len(A)):
        x0 = A[i]/ans
        x1 = A[i]/(ans+1)
        if ceil(x1)==x1:
            x1+=1
        if ceil(x1)>x0: break
        else:
            B.append(ceil(x1))
    cnt+=1
    if len(B) == len(A):
        sumB = sum(B[i] for i in range(len(B)))
        print(sumB)
        break
