def up_bow(l, r, x):
    while l < r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l 

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
gr, i = 0, 0
while i<n:
    while True:
        if i>=n : break
        next = up_bow(i+1, n, a[i]+k) # phần tử đầu tiên lớn hơn khoảng quy định 
        if next == i+1: break # Trả về i + 1 nếu không có phần tử hợp lệ do a[i + 1] > a[i + k]. Kết thúc chuyển nhóm mới
        else: i = next-1
    i+=1
    gr+=1
print(gr)