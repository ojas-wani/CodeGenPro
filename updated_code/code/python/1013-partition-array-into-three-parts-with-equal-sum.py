from typing import List

class Solution:
    """
    Given an array of integers `arr`, return `true` if we can partition the array into three non-empty parts with equal sums.
    """

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        """
        Return `true` if we can partition the array into three non-empty parts with equal sums.
        """
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        target_sum = total_sum // 3
        count = 0
        current_sum = 0
        
        for num in arr:
            current_sum += num
            if current_sum == target_sum:
                count += 1
                current_sum = 0
                if count == 2:
                    break
        
        return count == 2


# Remove trailing whitespace
__str__ = None
__repr__ = None