from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # Khởi tạo mảng dp với phần tử cuối là 0

        for i in range(n - 1, -1, -1):  # Duyệt ngược từ câu hỏi cuối cùng
            points, brainpower = questions[i]  # Lấy điểm và số câu bị bỏ qua
            next_index = i + brainpower + 1  # Chỉ mục của câu tiếp theo có thể làm

            # Nếu next_index nằm ngoài mảng, chỉ tính điểm hiện tại
            take = points + (dp[next_index] if next_index < n else 0)
            skip = dp[i + 1]  # Nếu bỏ qua câu này

            dp[i] = max(take, skip)  # Lựa chọn phương án tốt nhất
        
        return dp[0]  # Kết quả tối đa từ câu hỏi đầu tiên