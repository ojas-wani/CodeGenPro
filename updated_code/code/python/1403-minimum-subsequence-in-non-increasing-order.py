Python
from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """
        Given the array `nums`, obtain a subsequence of the array whose sum of elements is **strictly greater** than the sum of the non included elements in such subsequence.
        If there are multiple solutions, return the subsequence with **minimum size** and if there still exist multiple solutions, return the subsequence with the **maximum total sum** of all its elements.
        A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

        :param nums: A list of integers.
        :return: A list of integers which is a subsequence of `nums`.
        """
        nums.sort(reverse=True)
        total_sum = sum(nums)
        minsize = float('inf')
        maxsum = 0
        result = []
        subsequence_sum = 0
        for num in nums:
            if subsequence_sum + num > total_sum - subsequence_sum:
                if len(result) < minsize or (len(result) == minsize and subsequence_sum > maxsum):
                    result = [num]
                    maxsum = subsequence_sum
                    minsize = len(result)
                else:
                    result.append(num)
                    maxsum = subsequence_sum
                subsequence_sum += num
            else:
                break
        return result