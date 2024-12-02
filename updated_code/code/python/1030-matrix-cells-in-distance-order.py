Python
import heapq
from typing import List

class Solution:
    """
    This class provides a solution to the problem of sorting a 2D matrix in order of distance from a central cell.
    
    Parameters:
    rows (int): The number of rows in the matrix.
    cols (int): The number of columns in the matrix.
    rCenter (int): The row index of the central cell.
    cCenter (int): The column index of the central cell.
    
    Returns:
    List[List[int]]: A 2D list of cell coordinates sorted in order of distance from the central cell.
    """
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        This method returns the coordinates of all cells in the matrix, sorted by their distance from the central cell.
        
        Parameters:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        rCenter (int): The row index of the central cell.
        cCenter (int): The column index of the central cell.
        
        Returns:
        List[List[int]]: A 2D list of cell coordinates sorted in order of distance from the central cell.
        """
        # Generate all cell coordinates in the matrix
        cells = [(i, j) for i in range(rows) for j in range(cols)]
        
        # Calculate the distance of each cell from the central cell
        distances = [(abs(i - rCenter) + abs(j - cCenter), [i, j]) for i, j in cells]
        
        # Use a heap to sort the cells by their distance from the central cell
        sorted_cells = heapq.nsmallest(len(cells), distances)
        
        # Return the sorted cell coordinates
        return [cell for _, cell in sorted_cells]