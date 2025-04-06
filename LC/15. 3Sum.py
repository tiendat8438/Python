from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
            
        for i in range(len(nums) - 2):
            if nums[i] > 0:  # Dừng sớm nếu nums[i] > 0
                break
            if i > 0 and nums[i] == nums[i - 1]:  # Bỏ qua số trùng lặp
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:  
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res
