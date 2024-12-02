Python
from typing import List

class Solution:
    """
    This class contains a method to check if the given points are a boomerang.
    
    A boomerang is a set of three points that are all distinct and not in a straight line.
    
    The method takes a list of three points as input, where each point is a list of two integers representing the x and y coordinates.
    
    It returns True if the points are a boomerang and False otherwise.
    """

    def is_boomerang(self, points: List[List[int]]) -> bool:
        """
        This method checks if three points are a boomerang.
        
        A boomerang is a set of three points that are all distinct and not in a straight line.
        
        The method takes a list of three points as input, where each point is a list of two integers representing the x and y coordinates.
        
        It returns True if the points are a boomerang and False otherwise.
        """
        
        # Check if points are distinct
        if points[0][0] == points[1][0] or points[0][0] == points[2][0] or points[1][0] == points[2][0]:
            return False
        
        # Calculate slopes of lines formed by each pair of points
        slope12 = (points[1][1] - points[0][1]) * (points[2][0] - points[1][0]) - (points[2][1] - points[1][1]) * (points[1][0] - points[0][0])
        slope01 = (points[1][1] - points[0][1]) * (points[1][0] - points[0][0])
        
        # Check if the points are not in a straight line
        if slope12 == 0 and slope01 == 0:
            return False
        
        return True