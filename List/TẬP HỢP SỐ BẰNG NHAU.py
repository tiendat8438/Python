n, m = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
X = sorted(A)
Y = sorted(B)
if len(X) == len(Y):
    if all(X[i] == Y[i] for i in range(len(X))):
        print("YES")
    else: print("NO")
else: print("NO")