Python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        miss = 0
        while miss < k:
            if i not in arr:
                miss += 1
                if miss == k:
                    return i
            i += 1
        return None