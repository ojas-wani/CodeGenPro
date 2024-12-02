Python
from typing import List

class Solution:
    """
    Class with the solution.
    
    """

    def get_row(self, row_index: int) -> List[int]:
        """
        Returns the rowIndexth row of Pascal's triangle.
        
        Each number in the triangle is equal to the sum of the two numbers directly above it.
        
        :param row_index: The index of the row to be returned.
        :return: The rowIndexth row of Pascal's triangle.
        
        """
        row = [1]
        for _ in range(row_index):
            row = [x + y for x, y in zip([0]+row, row + [0])]
        return row