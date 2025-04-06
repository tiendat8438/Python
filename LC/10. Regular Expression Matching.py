# DP 2D
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p and p[0] == '*':  # Nếu `*` ở đầu => không hợp lệ
            return False  

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Hai chuỗi rỗng khớp nhau

        # Xử lý trường hợp p có dạng "a*" ngay từ đầu
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # Bỏ `x*`

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  # Khớp ký tự hoặc `.`

                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # Bỏ `x*`
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]  # Giữ `x*`

        return dp[m][n]
    
# DP 1D
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        curr = [False] * (n + 1)
        
        # Base case: Cả s và p đều rỗng
        prev[0] = True
        
        # Xử lý trường hợp p có ký tự '*'
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]

        # Duyệt từng ký tự của s
        for i in range(1, m + 1):
            curr[0] = False  # Khi p rỗng, s không thể khớp
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    curr[j] = prev[j - 1]  # Kế thừa trạng thái trước
                elif p[j - 1] == '*':
                    curr[j] = curr[j - 2]  # Bỏ `x*`
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        curr[j] |= prev[j]  # Giữ `x*` lặp lại nhiều lần
                else:
                    curr[j] = False  # Không khớp

            # Cập nhật dòng trước bằng dòng hiện tại
            prev, curr = curr, [False] * (n + 1)

        return prev[n]