Python
from typing import List

class Solution:
    """
    This class solves the problem of finding the sign of the product of an array.
    The sign of the product is determined by the sign of the first non-zero element if there are no zeros in the array.
    If there is a zero in the array, the sign of the product is zero.
    """
    def arraySign(self, nums: List[int]) -> int:
        """
        This method returns the sign of the product of all elements in the input array.
        
        Args:
        nums (List[int]): The input array of integers.
        
        Returns:
        int: The sign of the product of all elements in the input array.
        """
        zero_detected = False
        sign = 1
        
        # iterate over the input array
        for num in nums:
            if num == 0:
                # if we detect a zero, the sign of the product is 0
                zero_detected = True
            elif num < 0:
                # if we have a negative number, the sign of the product becomes negative
                sign *= -1
        
        # if we did not detect any zeros and the sign is 1, return 1
        # if we did not detect any zeros and the sign is -1, return -1
        # if we detected a zero, return 0
        return 1 if not zero_detected else 0 if sign == 1 else -1