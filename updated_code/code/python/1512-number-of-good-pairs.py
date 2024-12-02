Python
from typing import List

class Solution:

    """
    This class contains a method numIdenticalPairs that calculates the number of good pairs in an array of integers.
    
    A good pair is a pair of integers (i, j) that have the same value and i < j.
    
    Parameters:
    nums (List[int]): The list of integers.
    
    Returns:
    int: The number of good pairs.
    """

    """
    Calculate the number of good pairs in an array of integers.
    
    Parameters:
    nums (List[int]): The list of integers.
    
    Returns:
    int: The number of good pairs.
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Calculate the number of good pairs in an array of integers.
    
        Parameters:
        nums (List[int]): The list of integers.
    
        Returns:
        int: The number of good pairs.
        """
        count = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num == nums[j]:
                    count += 1
        return count