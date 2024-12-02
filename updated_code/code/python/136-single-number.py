from typing import List

class Solution:
    """
    This class is designed to solve the problem of finding the single number in an array where every element appears twice except for one.
    """
    """
    This method uses the XOR operation to find the single number in the array.
    The XOR operation has the property that a ^ a = 0 and any number a ^ 0 = a.
    So, when we XOR all the numbers in the array, the numbers that appear twice will cancel each other out, leaving the single number.
    """
    def single_number(self, nums: List[int]) -> int:
        """
        This function finds the single number in the array.
        It works by XORing all the numbers in the array.
        """
        result = 0
        for num in nums:
            result ^= num
        return result