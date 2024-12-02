Python
from typing import List

class Solution:
    """
    Docstring explaining the purpose of this class.
    This class contains a method to find the highest altitude of a point in a road trip.
    """
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Docstring explaining the purpose of this method.
        This method calculates the highest altitude of a point in a road trip.
        
        Parameters:
        gain (List[int]): A list of integers representing the net gain in altitude between points.
        
        Returns:
        int: The highest altitude of a point.
        """
        altitude = 0
        max_alt = 0
        for i, value in enumerate(gain):
            # Add gain of current point to the total altitude
            altitude += value
            # Update max_alt if current altitude is higher
            max_alt = max(max_alt, altitude)
        return max_alt