# Sliding window + Hashmap
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        used = {}
        for r in range(len(s)):
            if s[r] in used and used[s[r]] >= l:
                l = used[s[r]] + 1
            used[s[r]] = r
            max_len = max(max_len, r - l + 1)
        return max_len
    
# Slding window + Hashset
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        l = 0  # Con trỏ trái

        for r in range(len(s)):  # Con trỏ phải quét từng ký tự
            while s[r] in char_set:  # Nếu gặp ký tự trùng
                char_set.remove(s[l])  # Loại bỏ ký tự trái nhất
                l += 1  # Di chuyển con trỏ trái

            char_set.add(s[r])  # Thêm ký tự mới vào tập hợp
            max_len = max(max_len, r - l + 1)  

        return max_len