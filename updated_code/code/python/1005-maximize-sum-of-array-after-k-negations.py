from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        Given an integer array `nums` and an integer `k`, modify the array in the
        following way:

        * choose an index `i` and replace `nums[i]` with `-nums[i]`.
        
        You should apply this process exactly `k` times. You may choose the same index
        `i` multiple times.

        Return _the largest possible sum of the array after modifying it in this way_.
        
        """
        nums.sort()  # Sort the array in ascending order
        count = 0  # Count of negative numbers
        for num in nums:
            if num < 0:  # If number is negative
                count += 1  # Increment the count
                num = -num  # Flip the number
            if count >= k:  # If count of negative numbers is more than or equal to k
                break  # Stop the loop
            nums[nums.index(num)] = num  # Update the array with the flipped number
        if k % 2 == 1:  # If k is odd
            nums.sort(reverse=True)  # Sort the array in descending order
        return sum(nums)  # Calculate and return the sum