Python
from typing import List

class Solution:
    """
    This class defines a method to check if two string arrays are equal.
    
    Attributes:
        None
    """
    
    def array_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:
        """
        Given two string arrays `word1` and `word2`, return `True` if the two
        arrays **represent** the same string, and `False` otherwise.

        A string is **represented** by an array if the array elements concatenated
        **in order** forms the string.

        Parameters:
        word1 (List[str]): The first string array.
        word2 (List[str]): The second string array.

        Returns:
        bool: Whether the two string arrays are equal.
        """
        
        # Use the 'join' function to concatenate the elements in each array into strings
        str1 = ''.join(word1)
        str2 = ''.join(word2)
        
        # Compare the two strings
        return str1 == str2