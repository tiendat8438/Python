def find_min_triplet_sum(arr):
    n = len(arr)
    min_sum = float('inf')  # Khởi tạo tổng nhỏ nhất là vô cùng lớn
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_sum = arr[i] + arr[j] + arr[k]
                if current_sum < min_sum:
                    min_sum = current_sum
    return min_sum

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(find_min_triplet_sum(arr))