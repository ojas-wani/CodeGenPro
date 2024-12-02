"""
Module to determine if an array can be made strictly increasing by removing at most one element.
"""

from typing import List

class Solution:
    """
    Class to solve the problem of checking if an array can be made strictly increasing by removing at most one element.
    """

    def canBeIncreasing(self, nums: List[int]) -> bool:
        """
        Method to check if the array can be made strictly increasing by removing at most one element.
        """
        count = 0
        i = 1
        while i < len(nums):
            if nums[i-1] >= nums[i]:
                count += 1
                if count > 1:
                    return False
            i += 1
        return True