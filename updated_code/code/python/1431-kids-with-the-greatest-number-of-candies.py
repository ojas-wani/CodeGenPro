Python
from typing import List

class Solution:
    """
    This class is used to solve the problem of giving candies to kids.

    Attributes:
    None
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        This function returns a boolean array where each `result[i]` is `true` if,
        after giving the `ith` kid all the `extraCandies`, they will have the **greatest**
        number of candies among all the kids, or `false` otherwise.

        Args:
        candies (List[int]): An integer array where each `candies[i]` represents the number of candies the `ith` kid has.
        extraCandies (int): The number of extra candies that you have.

        Returns:
        List[bool]: A boolean array where each `result[i]` is `true` if, after giving the `ith` kid all the `extraCandies`, 
                    they will have the **greatest** number of candies among all the kids, or `false` otherwise.
        """
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]