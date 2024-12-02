"""
This is the solution for the Minimum Operations to Make the Array Increasing problem in LeetCode.

The problem is to find the minimum number of operations needed to make the array strictly increasing.

Each operation is incrementing an element in the array by 1.

The solution uses a simple iterate approach by counting the number of operations needed to make each element strictly increasing.

The function min_operations takes an array of integers as input and returns the minimum number of operations needed to make the array strictly increasing.
"""

from typing import List

class Solution:
    """
    This is the Solution class for the Minimum Operations to Make the Array Increasing problem in LeetCode.
    """

    def minOperations(self, nums: List[int]) -> int:
        """
        This is the minOperations function to find the minimum number of operations needed to make the array strictly increasing.
        
        :param nums: The input array of integers
        :return: The minimum number of operations needed to make the array strictly increasing
        """
        
        if len(nums) == 1:
            return 0
        
        operations = 0
        for i in range(len(nums) - 1):
            # Calculate the difference between the current element and the next element
            # If the difference is greater than 1, it means we need to increment the current element
            diff = max(0, nums[i+1] - nums[i] - 1)
            # Add the difference to the total operations
            operations += diff
        
        return operations