"""
Description:
Return an array of all the words that come immediately after "second" in each occurrence of "first second third", where "second" comes immediately after "first".
"""

from typing import List

class Solution:
    """
    This class provides a solution to find all the words that come immediately after "second" in each occurrence of "first second third".
    """
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        """
        This function finds all the words that come immediately after "second" in each occurrence of "first second third".
        
        Args:
            text (str): The input text where the occurrences are to be found.
            first (str): The word that comes before "second".
            second (str): The word that comes after "first" and before "third".
        
        Returns:
            List[str]: A list of words that come immediately after "second" in each occurrence of "first second third".
        """
        # Split the text into words
        words = text.split()
        
        # Initialize an empty list to store the result
        result = []
        
        # Iterate over the words
        for i in range(len(words) - 2):
            # Check if the current word is equal to "first" and the next word is equal to "second"
            if words[i] == first and words[i+1] == second:
                # If the condition is met, append the third word to the result list
                result.append(words[i+2])
        
        # Return the result list
        return result

# Add a newline at the end of the file