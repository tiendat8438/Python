# s = "PAYPALISHIRING" 
# exp: row = 3
# P   A   H   N
# A P L S I I G
# Y   I   R
# res = "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  # Không cần zigzag nếu chỉ có 1 hàng hoặc ít hơn số hàng yêu cầu
        
        rows = [""] * numRows  # Tạo danh sách lưu từng hàng
        index, step = 0, 1  # index là hàng hiện tại, step là hướng đi

        for char in s:
            rows[index] += char  # Thêm ký tự vào hàng tương ứng
            
            # Đảo chiều nếu chạm biên
            if index == 0:
                step = 1  # Xuống dưới
            elif index == numRows - 1:
                step = -1  # Lên trên
            
            index += step  # Cập nhật vị trí hàng
        
        return "".join(rows)  # Ghép tất cả hàng lại thành kết quả