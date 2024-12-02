Python
from typing import List

class Solution:
    """
    This is a class for solving the problem of sum of all subset XOR totals.
    """
    
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        This is a function to calculate the sum of all subset XOR totals for a given array of integers.
        
        Parameters:
        nums (List[int]): A list of integers.
        
        Returns:
        int: The sum of all subset XOR totals.
        """
        memo = {}
        def dfs(mask):
            if mask in memo:
                return memo[mask]
            res = 0
            for i, n in enumerate(nums):
                if mask & (1 << i):
                    res += dfs(mask ^ (1 << i)) ^ n
                else:
                    res += dfs(mask | (1 << i))
            memo[mask] = res
            return res
        return dfs(0)