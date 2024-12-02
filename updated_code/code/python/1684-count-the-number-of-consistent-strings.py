Python
"""
Description: This function counts the number of consistent strings in the given list of words.

A string is consistent if all its characters appear in the given allowed string.
"""

from typing import List

class Solution:
    """
    This class contains the function countConsistentStrings.
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Count the number of consistent strings in the given list of words.

        A string is consistent if all its characters appear in the given allowed string.

        Args:
            allowed (str): A string of allowed characters.
            words (List[str]): A list of strings.

        Returns:
            int: The number of consistent strings.
        """
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count