from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        This function takes a list of integers as input and returns a list where each element at index i is the number of elements in the input list that are smaller than the element at index i.
        """
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(sorted_nums.index(num))
        return result