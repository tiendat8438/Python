from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.checkCuts(rectangles, dim=0) or self.checkCuts(rectangles, dim=1)

    def checkCuts(self, rectangles: List[List[int]], dim: int) -> bool:
        gap_count = 0
        
        # Sắp xếp các hình chữ nhật theo tọa độ bắt đầu trong chiều đã chọn
        rectangles.sort(key=lambda r: r[dim])
        
        # Biến theo dõi điểm kết thúc xa nhất
        furthest_end = rectangles[0][dim + 2]
        
        # Duyệt qua từng hình chữ nhật sau hình đầu tiên
        for i in range(1, len(rectangles)):
            start = rectangles[i][dim]  # Tọa độ bắt đầu của hình hiện tại
            end = rectangles[i][dim + 2]  # Tọa độ kết thúc của hình hiện tại
            
            # Kiểm tra có khoảng trống giữa hai hình chữ nhật không
            if start >= furthest_end:
                gap_count += 1
            
            # Cập nhật điểm kết thúc xa nhất
            furthest_end = max(furthest_end, end)
            
            # Nếu có ít nhất 2 khoảng trống, trả về True
            if gap_count >= 2:
                return True
        
        return False
