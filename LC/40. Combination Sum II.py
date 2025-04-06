from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sắp xếp để loại bỏ số trùng dễ hơn

        def backtrack(start, path, cur_sum):
            if cur_sum == target:
                res.append(path[:])  # ✅ Lưu bản sao của `path`
                return
            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                # ✅ Loại bỏ số trùng lặp
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  
                
                path.append(candidates[i])
                backtrack(i + 1, path, cur_sum + candidates[i])  # Chỉ chọn số sau `i`
                path.pop()  # 🔙 Backtrack để thử tổ hợp khác

        backtrack(0, [], 0)
        return res
