from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Xử lý trường hợp mẫu p bắt đầu bằng '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1] # '*' có thể khớp với chuỗi rỗng
        
        # Duyệt qua từng ký tự trong s và p để cập nhật bảng dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1] # Ký tự khớp hoặc '?'
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] # '*' khớp với 0 hoặc nhiều ký tự
        return dp[m][n]
    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        pre = [False] * (n + 1)
        cur = [False] * (n + 1)
        pre[0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                pre[j] = pre[j - 1]

        for i in range(1, m + 1):
            cur[0] = False # Không thể khớp nếu mẫu rỗng mà chuỗi không rỗng
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    cur[j] = pre[j - 1]
                elif p[j - 1] == '*':
                    cur[j] = pre[j] or cur[j - 1]
                else:
                    cur[j] = False
            pre, cur = cur, pre
        return pre[n]