import typing

class Solution:
    """
    Given an array of integers `nums` and an integer `target`, 
    return _indices of the two numbers such that they add up to`target`.
    """
    def two_sum(self, nums: typing.List[int], target: int) -> typing.List[int]:
        """
        Return indices of the two numbers that add up to `target`.

        Args:
            nums (List[int]): An array of integers.
            target (int): The target sum.

        Returns:
            List[int]: Indices of the two numbers that add up to `target`.
        """
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i
        return []

# Your code has been rated at 10.00/10 (previous run: 0.00/10, +10.00)