"""
This module solves the problem of finding common characters in a list of strings.

The `commonChars` function takes a list of strings as input and returns a list of characters that are common to all strings.
"""
from collections import Counter
from typing import List

class Solution:
    """
    This class provides a solution for the problem of finding common characters in a list of strings.

    Attributes:
    - words: A list of strings
    """
    def common_chars(self, words: List[str]) -> List[str]:
        """
        This method finds the common characters in a list of strings.

        Args:
    - words: A list of strings

        Returns:
    - A list of characters that are common to all strings in the input list
        """
        # Initialize the counter with the first string
        counter = Counter(words[0])
        
        # Iterate over the remaining strings
        for word in words[1:]:
            # Update the counter with the intersection of the current counter and the counter of the current string
            counter &= Counter(word)
        
        # Initialize an empty list to store the result
        result = []
        
        # Iterate over the items in the counter
        for char, count in counter.items():
            # Extend the result list with the character repeated the specified number of times
            result.extend([char] * count)
        
        # Return the result
        return result