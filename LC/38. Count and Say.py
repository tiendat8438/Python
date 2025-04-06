from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            new_res = []
            i = 0
            while i < len(res):
                cnt = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    cnt += 1
                new_res.append(str(cnt))
                new_res.append(res[i])
                i += 1
            res = ''.join(new_res)
        return res