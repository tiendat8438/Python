# Stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Đánh dấu vị trí bắt đầu (tránh lỗi khi stack rỗng)
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':  # Nếu là '(' => đẩy vào stack
                stack.append(i)
            else:  # Nếu là ')'
                stack.pop()  # Bỏ phần tử trên cùng (tạo thành cặp '()' nếu có)

                if not stack:  # Nếu stack rỗng, đánh dấu vị trí lỗi
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])  # Tính độ dài dãy hợp lệ

        return max_len

# 2 con trỏ

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0

        # Duyệt từ trái sang phải
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0  # Reset nếu ')' quá nhiều

        left = right = 0

        # Duyệt từ phải sang trái
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0  # Reset nếu '(' quá nhiều

        return max_len
