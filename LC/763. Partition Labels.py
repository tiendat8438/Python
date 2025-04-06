from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {char : idx for idx, char in enumerate(s)}
        start, end = 0, 0
        partition = []
        for i, char in enumerate(s):
            end = max(end, last_idx[char])
            if i == end:
                partition.append(end - start + 1)
                start = i + 1
        return partition