from typing import List

class Solution:
    """
    This class is designed to check if the given points in a 2D plane form a straight line.
    
    Args:
    coordinates (List[List[int]]): A list of coordinates, where each coordinate is a list of two integers.
    
    Returns:
    bool: True if the points form a straight line, False otherwise.
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        This function checks if the given points in a 2D plane form a straight line.
        
        Args:
        coordinates (List[List[int]]): A list of coordinates, where each coordinate is a list of two integers.
        
        Returns:
        bool: True if the points form a straight line, False otherwise.
        """
        if len(coordinates) < 2:
            return True
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        if len(coordinates) == 2:
            return True  # Check for special case where there are only two points
        
        for x3, y3 in coordinates[2:]:
            if (y3 - y2) * (x2 - x1) != (y2 - y1) * (x3 - x2):
                return False
            y2, x2 = y3, x3
        
        return True
    
# Example usage
solution = Solution()
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(solution.checkStraightLine(coordinates))  # Output: True