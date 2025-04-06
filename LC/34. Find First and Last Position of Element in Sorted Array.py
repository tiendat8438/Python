from typing import List

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:  # Tìm về bên trái nếu nums[mid] == target
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    first = mid  # Ghi nhớ vị trí đầu tiên
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:  # Tìm về bên phải nếu nums[mid] == target
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    last = mid  # Ghi nhớ vị trí cuối cùng
            return last

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
