Python
"""
This is a Python class that calculates the length of the last word in a given string.

The class defines a method, `lengthOfLastWord`, which takes a string as an argument. 
It first removes leading and trailing spaces from the string using the `strip` method.
Then, it splits the string into a list of words using the `split` method. 
Finally, it returns the length of the last word in the list.

This code is designed to solve the problem described in the task, which is to find the length of the last word in a given string.
"""

class Solution:
    def length_of_last_word(self, s: str) -> int:
        """
        This method calculates the length of the last word in a given string.

        Args:
        s (str): The input string.

        Returns:
        int: The length of the last word in the string.
        """
        s = s.strip()  # Remove leading and trailing spaces
        words = s.split()  # Split the string into a list of words
        if len(words) == 0:  # If the list is empty
            return 0  # Return 0
        return len(words[-1])  # Return the length of the last word