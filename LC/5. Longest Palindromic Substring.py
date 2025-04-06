# Expand Around Center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not str:
            return ""
        def around_the_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        res = ''
        for i in range(len(s)):
            odd_palin = around_the_center(i, i)
            even_palin = around_the_center(i, i + 1)
            if len(odd_palin) > len(res):
                res = odd_palin
            if len(even_palin) > len(res):
                res = even_palin
        return res
                
# DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1  # Vị trí bắt đầu và độ dài của palindrome dài nhất

        # Mọi ký tự đơn lẻ là palindrome
        for i in range(n):
            dp[i][i] = True

        # Kiểm tra độ dài từ 2 trở lên
        for lenght in range(2, n + 1):
            for i in range(n - lenght + 1): # Vị trí bắt đầu
                j = i + lenght - 1 # Vị trí kết thúc
                if s[i] == s[j] and (lenght == 2 or dp[i + 1][j - 1]): # xử lý chuỗi ngắn (độ dài 1 hoặc 2)
                    dp[i][j] = True
                    if lenght > max_len:
                        start = i
                        max_len = lenght

        return s[start:start + max_len]  
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Bước 1: Chuyển đổi chuỗi ban đầu
        t = '#' + '#'.join(s) + '#'  # Biến đổi chuỗi
        n = len(t)
        p = [0] * n  # Mảng lưu bán kính palindrome
        center = right = 0  # Trung tâm & biên phải xa nhất
        max_length = 0
        start_index = 0

        # Bước 2: Duyệt từng ký tự trong transformed_s
        for i in range(n):
            mirror = 2 * center - i  # Vị trí đối xứng của i qua center
            
            if i < right:
                p[i] = min(right - i, p[mirror])  # Giới hạn bán kính
            
            # Bước 3: Mở rộng palindrome tại i
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            # Cập nhật center và right nếu mở rộng xa hơn
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Cập nhật palindrome dài nhất
            if p[i] > max_length:
                max_length = p[i]
                start_index = (i - p[i]) // 2  # Chuyển đổi về chỉ mục của chuỗi gốc

        # Trích xuất chuỗi con palindrome dài nhất từ s
        return s[start_index:start_index + max_length]