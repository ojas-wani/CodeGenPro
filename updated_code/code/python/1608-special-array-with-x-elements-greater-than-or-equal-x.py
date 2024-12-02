Python
from typing import List

class Solution:
    """
    A class to solve the problem of finding special numbers in an array.
    """
    
    def specialArray(self, nums: List[int]) -> int:
        """
        This function checks if the given array is special or not.
        A special array is defined as an array where there exists a number x
        such that there are exactly x numbers in the array that are greater than or equal to x.
        
        Args:
        nums (List[int]): The input array of integers.
        
        Returns:
        int: The special number x if the array is special, otherwise -1.
        """
        
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Iterate over the array from the end to the start
        for i in range(len(nums), 0, -1):
            # Check if the current number is greater than or equal to i
            # and if there are exactly i numbers in the array that are greater than or equal to i
            if i <= len(nums) and nums[i-1] >= i:
                # If the conditions are met, return the special number i
                return i
        
        # If no special number is found, return -1
        return -1