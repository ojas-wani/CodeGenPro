Python
from collections import Counter
from typing import List

# Add a description for the module
"""
This module contains a class that finds the sum of lengths of all good strings in a list
of words that can be formed by the characters in a given string.
"""

class Solution:
    """
    This class contains a method that solves the problem.
    """
    
    def count_characters(self, words: List[str], chars: str) -> int:
        """
        This method counts the sum of lengths of all good strings in a list of words
        that can be formed by the characters in a given string.

        Args:
        words (List[str]): A list of strings
        chars (str): A string of characters

        Returns:
        int: The sum of lengths of all good strings
        """
        chars_count = Counter(chars)
        total_count = 0
        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= chars_count[char] for char in word_count):
                total_count += len(word)
        return total_count

# Add two blank lines between the class definition and the main block of code