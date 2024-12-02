Python
from typing import List

class Solution:
    """
    Given an array `nums`, return `true` if the array was originally sorted in
    non-decreasing order, then rotated **some** number of positions (including
    zero). Otherwise, return `false`.

    There may be **duplicates** in the original array.

    **Note:** An array `A` rotated by `x` positions results in an array `B` of the
    same length such that `A[i] == B[(i+x) % A.length]`, where `%` is the modulo
    operation.
    """

    def check(self, nums: List[int]) -> bool:
        """
        Check if the array was originally sorted in non-decreasing order, then
        rotated **some** number of positions (including zero).
        """
        if len(nums) <= 1:
            return True

        # Check if the array is sorted
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False

        # Check if the array has been rotated
        if nums[0] >= nums[-1]:
            return False

        return True