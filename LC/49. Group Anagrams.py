from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        from collections import defaultdict
        mapping = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            mapping[key].append(word)
        return list(mapping.values())