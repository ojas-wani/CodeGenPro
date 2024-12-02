"""
Description:
This problem is about removing duplicate adjacent letters in a string.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move. 
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""

class Solution:
    """
    A solution class for the problem.
    """
    def remove_duplicates(self, s: str) -> str:
        """
        This function removes duplicate adjacent letters in a string.

        Args:
        s (str): The input string.

        Returns:
        str: The string with duplicate adjacent letters removed.
        """
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)