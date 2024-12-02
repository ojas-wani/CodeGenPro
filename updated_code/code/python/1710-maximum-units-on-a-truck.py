"""
This module provides a solution to the problem of finding the maximum total number of units that can be put on a truck.
The truck has a maximum capacity in terms of the number of boxes it can carry. The boxes have different types and contain different numbers of units.
The goal is to find the combination of boxes that maximizes the total number of units that can be carried on the truck.
"""

from typing import List

class Solution:
    """
    This class provides a solution to the problem of finding the maximum total number of units that can be put on a truck.
    """

    def maximum_units(self, box_types: List[List[int]], truck_size: int) -> int:
        """
        This method finds the maximum total number of units that can be put on the truck.
        
        Parameters:
        box_types (List[List[int]]): A 2D list where each inner list contains the number of boxes and units per box.
        truck_size (int): The maximum number of boxes that can be carried on the truck.
        
        Returns:
        int: The maximum total number of units that can be put on the truck.
        """
        
        # Sort the box_types based on the number of units per box in descending order
        box_types.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        for num_boxes, num_units in box_types:
            # If the number of boxes is less than or equal to the truck size, add the number of boxes multiplied by the number of units per box to the total units
            if num_boxes <= truck_size:
                total_units += num_boxes * num_units
                truck_size -= num_boxes
            # If the number of boxes is more than the truck size, add the remaining truck size multiplied by the number of units per box to the total units and break the loop
            else:
                total_units += truck_size * num_units
                truck_size = 0
                break
        
        return total_units