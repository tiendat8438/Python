def find(n, k):
    if n == 1: # Nếu N = 1, ký tự duy nhất là 'A'
        return 'A'
    # Độ dài của xâu S ở bước N-1
    length = 2 ** (n - 1) - 1
    if k == length + 1:  # Nếu K nằm ở giữa xâu
        return chr(ord('A') + n - 1)
    if k <= length: # Nếu K nằm ở nửa đầu
        return find(n - 1, k)
    # Nếu K nằm ở nửa sau
    return find(n - 1, k - length - 1)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(find(n, k))
