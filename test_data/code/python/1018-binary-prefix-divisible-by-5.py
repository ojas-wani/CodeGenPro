from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        temp = 0
        for num in nums:
            temp = (temp * 2 + num) % 5
            res.append(temp == 0)
        return res