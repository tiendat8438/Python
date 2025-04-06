from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def Try(start, path, cur_sum):
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                Try(i, path, cur_sum + candidates[i])
                path.pop()

        Try(0, [], 0)
        return res

