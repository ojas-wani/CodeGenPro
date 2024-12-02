from typing import List

class Solution:
    """
    This class is used to find the running sum of a given array.
    
    Attributes:
    None
    """
    
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        This method is used to calculate the running sum of a given array.
        
        Args:
        nums (List[int]): The input array.
        
        Returns:
        List[int]: The running sum of the input array.
        """
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result