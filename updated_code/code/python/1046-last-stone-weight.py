Python
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        This function calculates the weight of the last remaining stone.
        
        Parameters:
        stones (List[int]): A list of integer weights of stones.
        
        Returns:
        int: The weight of the last remaining stone. If there are no stones left, return 0.
        """
        # Create a max heap from the stones
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)  # Use negative stone weight for max heap
        
        while len(heap) > 1:
            # Pop the two heaviest stones from the heap
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                # If the stones are not equal, push the new stone weight back into the heap
                heapq.heappush(heap, -(y - x))
        
        # Return the weight of the last remaining stone
        return -heapq.heappop(heap) if heap else 0