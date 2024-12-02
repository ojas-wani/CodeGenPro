from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        operations = 0
        for i in range(len(nums) - 1):
            operations += max(0, nums[i+1] - nums[i] - 1)
        return operations