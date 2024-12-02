from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted((x, i) for i, x in enumerate(arr))
        rank = {}
        for x, _ in sorted_arr:
            if x not in rank:
                rank[x] = len(rank) + 1
        return [rank[x] for x in arr]