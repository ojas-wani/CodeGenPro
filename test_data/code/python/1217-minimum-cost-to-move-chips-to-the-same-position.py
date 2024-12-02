class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count, res = 0, float('inf')
        for x in set(position):
            count = position.count(x)
            if count <= res:
                res = count
        return min(res, len(position) - res)