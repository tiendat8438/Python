n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

X = sorted(A & B)  # Giao của A và B, sắp xếp tăng dần
Y = sorted(A - B)  # Phần tử có trong A nhưng không có trong B
Z = sorted(B - A)  # Phần tử có trong B nhưng không có trong A
    
print(" ".join(map(str, X)))
print(" ".join(map(str, Y)))
print(" ".join(map(str, Z)))
