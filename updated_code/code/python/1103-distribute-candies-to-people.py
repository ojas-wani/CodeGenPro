Python
from typing import List

class Solution:
    """
    This class is used to distribute candies among num_people.
    
    Attributes:
    None
    
    Methods:
    distributeCandies: This method takes two arguments, candies and num_people, 
                       and returns a list of candies distributed among num_people.
    """

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        This method distributes candies among num_people.
        
        Args:
        candies (int): The total number of candies to be distributed.
        num_people (int): The number of people to distribute the candies.

        Returns:
        List[int]: A list of candies distributed among num_people.
        """
        res = [0] * num_people
        i, x = 0, 1
        while candies > 0:
            if candies >= x:
                res[i] += x
                candies -= x
                x += 1
            else:
                res[i] += candies
                candies = 0
            if i == num_people - 1:
                i = 0
            else:
                i += 1
        return res