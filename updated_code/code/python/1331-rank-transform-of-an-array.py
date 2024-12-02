"""
This module provides a solution for the 'Rank Transform of an Array' problem.
Given an array of integers, replace each element with its rank.

The rank represents how large the element is. The rank has the following
rules:

  * Rank is an integer starting from 1.
  * The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
  * Rank should be as small as possible.
"""
from typing import List

class Solution:
    """
    This class provides a solution for the 'Rank Transform of an Array' problem.
    """
    def array_rank_transform(self, arr: List[int]) -> List[int]:
        """
        Replaces each element in the input array with its rank.

        Args:
            arr (List[int]): Input array of integers.

        Returns:
            List[int]: Output array with each element replaced with its rank.
        """
        # Sort the array and keep track of the indices
        sorted_arr = sorted((x, i) for i, x in enumerate(arr))

        # Initialize the rank dictionary
        rank = {}

        # Calculate the rank for each element
        for _, i in sorted_arr:
            if i not in rank:
                rank[i] = len(rank) + 1

        # Return the output array with each element replaced with its rank
        return [rank[i] for i, _ in enumerate(arr)]