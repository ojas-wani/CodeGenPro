from typing import List

class Solution:
    """
    This class provides a solution to the "replace elements with the greatest element on the right side problem".
    
    The function replaceElements(self, arr: List[int]) -> List[int] takes a list of integers as input, 
    replaces every element in that array with the greatest element among the elements to its right, 
    and replaces the last element with -1. Finally, it returns the modified array.
    """

    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        This function replaces every element in the input array with the greatest element among 
        the elements to its right, and replaces the last element with -1.
        
        Param: arr (List[int]) - The input array.
        
        Return: List[int] - The modified array.
        """

        n = len(arr)
        i = n - 1
        max_to_right = -1  # Initialize max_to_right with -1
        
        if n == 1:  # If the array has only one element, return -1.
            return [-1]
        
        # Replace every element in the array with the greatest element among the elements to its right.
        while i >= 0:
            temp = arr[i]  # Assign the current element to a temporary variable.
            arr[i] = max_to_right  # Replace the current element with max_to_right.
            if i < n - 1:
                max_to_right = max(max_to_right, arr[i + 1])  # Update max_to_right.
            i -= 1
        
        return arr