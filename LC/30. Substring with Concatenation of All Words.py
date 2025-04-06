from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)  # Đếm số lần xuất hiện của mỗi từ trong `words`
        res = []

        # Duyệt từng vị trí bắt đầu có thể hợp lệ
        for i in range(word_len):
            left = i  # Điểm bắt đầu cửa sổ trượt
            right = i
            cur_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]  # Lấy từ có độ dài `word_len`
                right += word_len

                if word in word_count:
                    cur_count[word] += 1

                    while cur_count[word] > word_count[word]:  # Nếu quá số lượng cho phép, di chuyển `left`
                        cur_count[s[left:left + word_len]] -= 1
                        left += word_len

                    if right - left == total_len:  # Nếu cửa sổ có đúng `total_len`, lưu kết quả
                        res.append(left)

                else:  # Nếu gặp từ không hợp lệ, reset cửa sổ
                    cur_count.clear()
                    left = right

        return res

# Test
sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Output: [0, 9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # Output: []
