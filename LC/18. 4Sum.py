from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Bỏ qua số trùng lặp
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # Cắt sớm
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:  # Không thể đạt target
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Bỏ qua số trùng lặp
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:  # Cắt sớm
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:  # Không thể đạt target
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:  
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:  
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

