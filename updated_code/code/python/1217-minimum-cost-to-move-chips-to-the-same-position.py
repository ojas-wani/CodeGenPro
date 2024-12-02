Python
from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        Return the minimum cost needed to move all the chips to the same position.
        """
        # Initialize minimum cost and the frequency of each position
        min_cost = float('inf')
        freq = {}

        # Count the frequency of each position
        for pos in position:
            if pos in freq:
                freq[pos] += 1
            else:
                freq[pos] = 1

        # Calculate the minimum cost
        for pos, count in freq.items():
            cost = min(pos % 2, len(position) - pos % 2)
            min_cost = min(min_cost, cost)

        return min_cost