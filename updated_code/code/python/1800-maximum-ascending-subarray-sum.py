Python
from typing import List

class Solution:
    """
    Given an array of positive integers nums, return the maximum possible sum of an **ascending** subarray in `nums`.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray `[numsl, numsl+1, ..., numsr-1, numsr]` is **ascending** if for all `i` where `l <= i < r`, `numsi  < numsi+1`. Note that a subarray of size `1` is **ascending**.

    Example 1:
        Input: nums = [10,20,30,5,10,50]    Output: 65    Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

    Example 2:
        Input: nums = [10,20,30,40,50]    Output: 150    Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

    Example 3:
        Input: nums = [12,17,15,13,10,11,12]    Output: 33    Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

    Constraints:
        * `1 <= nums.length <= 100`
        * `1 <= nums[i] <= 100`
    """
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        This function calculates the maximum possible sum of an ascending subarray.
        
        Args:
            nums (List[int]): A list of positive integers.
        
        Returns:
            int: The maximum possible sum of an ascending subarray.
        """
        max_sum, dp = 0, [0]  # Initialize `max_sum` as 0 and `dp` as a list of 0s
        
        for num in nums:  # Iterate through the list of numbers
            if dp[-1] + num > num:  # Check if the current number is greater than the previous sum
                dp[-1] += num  # If true, add the current number to the previous sum
            else:
                dp.append(num)  # If not, add the current number to the list and calculate the sum from the start
            max_sum = max(max_sum, max(dp))  # Update the maximum sum
        
        return max_sum  # Return the maximum sum