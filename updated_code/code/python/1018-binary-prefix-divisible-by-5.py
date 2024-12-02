"""
Module to solve the problem of prefixes divisible by 5 in binary array.

This module defines a class `Solution` with a method `prefixes_divisible_by_5` that takes a list of binary numbers as input and returns a list of booleans indicating whether each prefix is divisible by 5.

"""
class Solution:
    """
    Class to solve the problem of prefixes divisible by 5 in binary array.
    
    Attributes:
    None
    
    Methods:
    prefixes_divisible_by_5(nums): Returns a list of booleans indicating whether each prefix in the input array is divisible by 5.
    """
    def prefixes_divisible_by_5(self, nums: List[int]) -> List[bool]:
        """
        Method to determine if each prefix in the input array is divisible by 5.

        Args:
        nums (List[int]): A list of binary numbers.

        Returns:
        List[bool]: A list of booleans indicating whether each prefix is divisible by 5.
        """
        res = []
        temp = 0
        for num in nums:
            temp = (temp * 2 + num) % 5
            res.append(temp == 0)
        return res