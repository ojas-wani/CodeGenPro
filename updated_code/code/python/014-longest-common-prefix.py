Python
from typing import List

class Solution:
    """
    This class contains the solution for the longest common prefix problem.
    
    The longest common prefix problem is to find the prefix that is common to all the strings in the input array.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        This function finds the longest common prefix among an array of strings.
        
        Parameters:
        strs (List[str]): A list of strings.
        
        Returns:
        str: The longest common prefix.
        """
        if not strs:
            return ""
        
        prefix = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        
        return prefix

# Test cases
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""