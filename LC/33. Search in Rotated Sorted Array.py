from typing import List

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Tìm vị trí giữa
            
            if nums[mid] == target:
                return mid  # Tìm thấy target
            
            # Kiểm tra xem nửa nào đã sắp xếp
            if nums[left] <= nums[mid]:  # Nửa trái đã sắp xếp
                if nums[left] <= target < nums[mid]:  # Target nằm trong nửa trái
                    right = mid - 1
                else:
                    left = mid + 1  # Target nằm trong nửa phải
            else:  # Nửa phải đã sắp xếp
                if nums[mid] < target <= nums[right]:  # Target nằm trong nửa phải
                    left = mid + 1
                else:
                    right = mid - 1  # Target nằm trong nửa trái
        
        return -1  # Không tìm thấy target
