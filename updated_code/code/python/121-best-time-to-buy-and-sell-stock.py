Python
from typing import List

class Solution:
    """
    A class that solves the problem of finding the maximum profit from buying and selling a stock once.

    Attributes:
        max_profit (int): The maximum profit that can be achieved from buying and selling a stock once.

    Methods:
        maxProfit(prices: List[int]) -> int: The maximum profit that can be achieved from buying and selling a stock once.
    """

    def __init__(self):
        """
        Initializes the solution.
        """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit that can be achieved from buying and selling a stock once.

        Args:
            prices (List[int]): A list of prices of a stock on different days.

        Returns:
            int: The maximum profit that can be achieved from buying and selling a stock once.
        """
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit