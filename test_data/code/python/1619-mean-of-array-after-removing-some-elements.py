from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        total = sum(arr)
        arr = arr[n//20[:-5]:n//20[5:]]
        return total / len(arr)