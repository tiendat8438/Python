from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')

        for i in range(len(nums) - 2):
            # Có thể bỏ nếu không muốn tối ưuưu
            """# Nếu tổng nhỏ nhất đã lớn hơn target, không cần xét nữa
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                if abs(nums[i] + nums[i + 1] + nums[i + 2] - target) < abs(ans - target):
                    ans = nums[i] + nums[i + 1] + nums[i + 2]
                break  
            
            # Nếu tổng lớn nhất nhỏ hơn target, cập nhật ans rồi bỏ qua vòng lặp
            if nums[i] + nums[-1] + nums[-2] < target:
                if abs(nums[i] + nums[-1] + nums[-2] - target) < abs(ans - target):
                    ans = nums[i] + nums[-1] + nums[-2]
                continue  
            
            # Bỏ qua phần tử trùng lặp để tránh lặp lại kết quả
            if i > 0 and nums[i] == nums[i - 1]:
                continue  """

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == target:
                    return total  # Tìm thấy tổng chính xác, trả về ngay

                # Cập nhật `ans` nếu `total` gần với target hơn
                if abs(total - target) < abs(ans - target):
                    ans = total

                if total < target:
                    l += 1
                else:
                    r -= 1

        return ans
