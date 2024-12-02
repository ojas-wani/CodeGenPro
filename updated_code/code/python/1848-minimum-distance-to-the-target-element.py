class Solution:
    """
    Given an integer array `nums` (0-indexed) and two integers `target` and `start`, 
    find an index `i` such that `nums[i] == target` and `abs(i - start)` is minimized.
    
    Return `abs(i - start)`.
    """
    def get_min_distance(self, nums: list, target: int, start: int) -> int:
        """
        Find the minimum distance to the target element in the array.
        
        Args:
        nums (list): The input array.
        target (int): The target element.
        start (int): The starting index.
        
        Returns:
        int: The minimum distance to the target element.
        """
        min_distance = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                min_distance = min(min_distance, abs(i - start))
        return min_distance