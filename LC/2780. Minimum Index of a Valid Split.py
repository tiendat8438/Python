from typing import List

# Sử dụng Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter
        # Bước 1: Tìm phần tử chiếm ưu thế
        freq = Counter(nums)
        dominant = max(freq, key=freq.get)
        total_count = freq[dominant]
        # Bước 2: Duyệt mảng để tìm vị trí chia hợp lệ
        left_count = 0 # Số lần xuất hiện của dominant trong phần bên trái
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
            # Số lần xuất hiện của dominant trong phần bên trái
            left_valid = left_count * 2 > (i + 1)
            right_valid = (total_count - left_count) * 2 > (n - i - 1)
            if left_valid and right_valid:
                return i
        return -1


# Sử dụng Boyer-Moore Majority Vote: Tối ưu hóa bộ nhớ hơn
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        candidate, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += (1 if num == candidate else -1)
        
        total_count = sum(1 for num in nums if num == candidate)
        if total_count * 2 <= n:
            return -1

        left_count = 0
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            left_valid = left_count * 2 > (i + 1)
            right_valid = (total_count - left_count) * 2 > (n - i - 1)
            if left_valid and right_valid:
                return i
        return -1
