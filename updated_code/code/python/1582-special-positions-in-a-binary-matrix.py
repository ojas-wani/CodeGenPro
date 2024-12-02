Python
from typing import List

class Solution:
    """
    This class defines a method to return the number of special positions in a given binary matrix.
    
    A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
    """

    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        This method takes a binary matrix as input and returns the number of special positions in the matrix.
        
        A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
        
        Parameters:
        mat (List[List[int]]): The given binary matrix
        
        Returns:
        int: The number of special positions in the matrix
        """
        
        # Initialize the count of special positions
        special_positions = 0
        
        # Get the number of rows and columns in the matrix
        m, n = len(mat), len(mat[0])
        
        # Iterate over each cell in the matrix
        for i in range(m):
            for j in range(n):
                # If the current cell is 1
                if mat[i][j] == 1:
                    # Check if all other cells in the same row and column are 0
                    if all(mat[x][j] == 0 for x in range(m) if x != i) and all(mat[i][y] == 0 for y in range(n) if y != j):
                        # If all conditions are met, increment the count of special positions
                        special_positions += 1
        
        # Return the count of special positions
        return special_positions