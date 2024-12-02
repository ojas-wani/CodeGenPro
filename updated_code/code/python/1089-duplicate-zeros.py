Python
from typing import List

class Solution:
    """
    Description: 
    This class is used to solve the problem of 
    duplicating each occurrence of zero in a given 
    fixed-length integer array `arr`, shifting the 
    remaining elements to the right.

    """
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Method: duplicateZeros
        Description: 
        This method does not return anything, 
        it modifies the array in-place instead.

        Parameters: 
        arr (List[int]): The given fixed-length 
                         integer array.

        """
        i = 0
        n = len(arr) - 1  # Naming convention is snake_case, it's more Pythonic.

        while i < n:
            if arr[i] == 0:
                for j in range(n, i, -1):
                    arr[j] = arr[j-1]
                arr[i+1] = 0
                i += 1
                n -= 1
            else:
                i += 1

# Adding a new line at the end of the file on Python.