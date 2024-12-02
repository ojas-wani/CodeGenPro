from typing import List
class Solution:
    def solution(self, arr: List[int]) -> bool:
        """
        Checks if an array can be rearranged to form an arithmetic progression.

        Args:
            arr (List[int]): The input array.

        Returns:
            bool: True if the array can be rearranged to form an arithmetic progression, False otherwise.
        """

        arr.sort()

        diff = (arr[1] - arr[0]) if len(arr) > 1 else None
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True