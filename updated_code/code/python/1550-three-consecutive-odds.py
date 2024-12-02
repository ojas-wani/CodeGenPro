from typing import List

class ThreeConsecutiveOdds:
    """
    Given an integer array `arr`, return `true` if there are three consecutive odd
    numbers in the array. Otherwise, return `false`.
    """

    def three_consecutive_odds(self, arr: List[int]) -> bool:
        """
        Check if there are three consecutive odd numbers in the array.

        Args:
            arr (List[int]): The input array.

        Returns:
            bool: True if there are three consecutive odd numbers, False otherwise.
        """
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False