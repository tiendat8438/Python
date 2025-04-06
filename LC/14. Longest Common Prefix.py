from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        cur_s = strs[0]
        for word in strs[1:]:
            while not word.startswith(cur_s):
                cur_s = cur_s[:-1]
                if not cur_s:
                    return ""

        return cur_s
