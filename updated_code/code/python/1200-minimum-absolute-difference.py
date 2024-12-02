from typing import List

class Solution:
    """
    This class provides a method to find all pairs of elements with the minimum absolute difference of any two elements in the array.
    """
    
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        This method sorts the input array and then iterates over the sorted array to find the minimum absolute difference between adjacent elements.
        If the minimum difference is found, it adds all pairs with this difference to the result list.
        """
        arr.sort()
        min_diff = float('inf')
        result = []
        
        # Iterate over the sorted array to find the minimum absolute difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i-1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result