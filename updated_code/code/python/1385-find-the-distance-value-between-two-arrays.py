from typing import List

class Solution:
    """
    This class defines a solution to find the distance value between two arrays.
    """
    """
    This method finds the distance value between two arrays.
    
    Parameters:
    arr1 (List[int]): The first array.
    arr2 (List[int]): The second array.
    d (int): The distance value.
    
    Returns:
    int: The distance value.
    """
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Initialize the count variable to 0.
        """
        count = 0
        
        """
        Iterate over each number in the first array.
        """
        for num in arr1:
            """
            Initialize a flag to True.
            """
            flag = True
            
            """
            Iterate over each number in the second array.
            """
            for num2 in arr2:
                """
                If the absolute difference between the two numbers is less than or equal to d, set the flag to False and break the loop.
                """
                if abs(num - num2) <= d:
                    flag = False
                    break
            
            """
            If the flag is True, it means there is no number in the second array within d distance from the current number in the first array.
            Increment the count.
            """
            if flag:
                count += 1
        
        """
        Return the count.
        """
        return count