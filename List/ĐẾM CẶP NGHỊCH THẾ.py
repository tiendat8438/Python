def merge_and_count(arr, temp_arr, left, mid, right):
    i = left     # Chỉ mục của mảng con trái
    j = mid + 1  # Chỉ mục của mảng con phải
    k = left     # Chỉ mục của mảng tạm
    inv_count = 0  # Biến đếm số nghịch thế

    # Duyệt hai nửa mảng và gộp lại
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Tất cả phần tử còn lại của bên trái sẽ tạo nghịch thế
            j += 1
        k += 1

    # Sao chép các phần tử còn lại của nửa trái (nếu có)
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Sao chép các phần tử còn lại của nửa phải (nếu có)
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Sao chép lại vào mảng chính
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        # Đếm nghịch thế bên trái, bên phải và khi trộn
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

# Đọc input và chạy thuật toán
n = int(input())
arr = list(map(int, input().split()))
temp_arr = [0] * n  # Mảng tạm để hỗ trợ merge sort
print(merge_sort_and_count(arr, temp_arr, 0, n - 1))
