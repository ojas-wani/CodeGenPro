class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        """
        This function finds the kth missing positive integer in a sorted array.

        Args:
        arr (list): A sorted list of positive integers.
        k (int): The position of the missing positive integer.

        Returns:
        int: The kth missing positive integer.
        """
        i, miss = 0, 0
        for num in range(1, max(arr) + k + 1):
            if miss == k:
                return num
            if num not in arr:
                miss += 1
            i += 1
        return None