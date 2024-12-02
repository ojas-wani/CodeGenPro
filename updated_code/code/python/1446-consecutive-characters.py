Python
class Solution:
    """
    This class is used to solve the problem of finding the maximum power of a string.
    
    Attributes:
    None
    """

    def max_power(self, s: str) -> int:
        """
        This method calculates the maximum power of a string.
        
        Parameters:
        s (str): The input string.
        
        Returns:
        int: The maximum power of the string.
        """
        max_power = 0
        i = 0
        if not s:  # Handle empty string
            return 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            max_power = max(max_power, count)
            i += 1
        return max_power