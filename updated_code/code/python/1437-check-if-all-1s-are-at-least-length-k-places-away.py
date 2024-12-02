from typing import List

class Solution:
    """
    This class contains a method to check if all 1s are at least k places away from each other in a binary array.

    Args:
        nums (List[int]): A binary array of 0s and 1s.
        k (int): The minimum distance required between 1s.

    Returns:
        bool: True if all 1s are at least k places away from each other, False otherwise.
    """
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        This method checks if all 1s are at least k places away from each other in a binary array.

        Args:
            nums (List[int]): A binary array of 0s and 1s.
            k (int): The minimum distance required between 1s.

        Returns:
            bool: True if all 1s are at least k places away from each other, False otherwise.
        """
        prev_one = -1
        for i, num in enumerate(nums):
            if num == 1:
                if prev_one != -1 and i - prev_one <= k:
                    return False
                prev_one = i
        return True