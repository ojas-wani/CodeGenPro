from typing import List

class Solution:
    """
    Description: Given a sorted array of distinct integers and a target value,
                 return the index if the target is found. If not, return the index
                 where it would be if it were inserted in order.

    :param nums: A sorted array of distinct integers.
    :type nums: List[int]
    :param target: The target value to search for.
    :type target: int
    :return: The index if the target is found, or the index where it would be inserted.
    :rtype: int
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary search algorithm to find the target value in the sorted array.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left