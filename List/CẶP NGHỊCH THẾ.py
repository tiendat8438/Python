# N = int(input())
# arr = list(map(int, input().split()))
# cnt = 0
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if arr[i] > arr[j]:
#             cnt += 1
# print(cnt)

# trường hợp n lớn
def count_inversions(arr):
    # Hàm merge_sort trả về số lượng cặp nghịch thế và mảng đã sắp xếp
    def merge_sort(arr):
        if len(arr) <= 1:
            return 0, arr

        mid = len(arr) // 2
        left_count, left_sorted = merge_sort(arr[:mid])
        right_count, right_sorted = merge_sort(arr[mid:])
        merge_count, merged = merge(left_sorted, right_sorted)

        total = left_count + right_count + merge_count
        return total, merged

    # Hàm merge trả về số lượng cặp nghịch thế và mảng đã merge
    def merge(left, right):
        result = []
        i = j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                count += len(left) - i  # Đếm số cặp nghịch thế

        result.extend(left[i:])
        result.extend(right[j:])

        return count, result

    total_inversions, _ = merge_sort(arr)
    return total_inversions


# Đọc input
N = int(input())
A = list(map(int, input().split()))

# Đếm số lượng cặp nghịch thế
result = count_inversions(A)

# In kết quả
print(result)
