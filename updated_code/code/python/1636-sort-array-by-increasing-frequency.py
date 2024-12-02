Python
from collections import Counter
from typing import List

class Solution:
    """
    This class provides a method to sort an array of integers based on their frequency.
    The frequency of the values in the array is calculated first, then the array is sorted
    based on the frequency in increasing order and the values themselves in decreasing order.
    """
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Method to sort the array of integers based on their frequency.

        Args:
        nums (List[int]): The input array of integers.

        Returns:
        List[int]: The sorted array of integers.
        """
        # Calculate the frequency of each value in the array
        count = Counter(nums)
        
        # Sort the values based on their frequency in increasing order, and
        # themselves in decreasing order
        sorted_nums = sorted(count.items(), key=lambda x: (x[1], -x[0]))
        
        # Initialize an empty list to store the sorted array
        result = []
        
        # Add the sorted values to the result list
        for num, freq in sorted_nums:
            result.extend([num] * freq)
        
        return result