used, A = [], []
global cnt

def Try(pre, sum, idx, n, target):
    global cnt  # Cần khai báo biến toàn cục để tránh lỗi
    if sum > target:
        return
    if idx == 2:  # Nếu đã chia được 2 phần thì phần còn lại chắc chắn hợp lệ
        cnt += 1
        return
    if sum == target:
        return Try(0, 0, idx + 1, n, target)
    for i in range(pre, n):
        if used[i]:
            used[i] = 0
            Try(i + 1, sum + A[i], idx, n, target)  # Thứ tự tham số đúng
            used[i] = 1
    return

for _ in range(int(input())):
    n = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)  # Sắp xếp giảm dần để tối ưu
    total = sum(A)
    
    if total % 3 != 0:
        print(0)
        continue
    
    target = total // 3
    if A[0] > target:  # Nếu phần tử lớn nhất lớn hơn target thì không thể chia
        print(0)
        continue
    
    used = [1] * n
    cnt = 0
    Try(0, 0, 0, n, target)
    print(cnt)
