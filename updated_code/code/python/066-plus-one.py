Python
from typing import List

class Solution:
    """
    This class is used to increment the large integer represented as an integer array by one.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increment the large integer by one and return the resulting array of digits.

        Args:
            digits (List[int]): The array of digits representing the large integer.

        Returns:
            List[int]: The resulting array of digits after incrementing by one.
        """
        # Iterate from the most significant digit to the least significant digit
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, increment it by 1 and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and move to the next digit
            else:
                digits[i] = 0
        # If all digits are 9, add a new digit 1 to the most significant position
        return [1] + digits