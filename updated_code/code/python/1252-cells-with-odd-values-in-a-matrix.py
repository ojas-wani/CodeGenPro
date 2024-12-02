from typing import List

class Solution:
    def oddCells(self, rows: int, cols: int, indices: List[List[int]]) -> int:
        """
        This function simulates the given operations on a m x n matrix and count the total number of odd cells.
        
        Parameters:
        m (int): The number of rows in the matrix
        n (int): The number of columns in the matrix
        indices (List[List[int]]): A list of locations where increment operation will be performed
        
        Returns:
        int: The total number of odd cells in the matrix after the operations
        """
        
        rows_value = [0] * rows
        cols_value = [0] * cols
        
        # Perform increment operation for each location in indices
        for r, c in indices:
            rows_value[r] += 1
            cols_value[c] += 1
        
        # Count the total number of odd cells
        count = sum(1 for row in range(rows) for col in range(cols) if (rows_value[row] + cols_value[col]) % 2 != 0)
        
        return count