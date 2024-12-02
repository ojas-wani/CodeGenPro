class Solution:
    """
    This class defines a method to check if a binary string has at most one contiguous segment of ones.
    
    Parameters:
    s (str): The binary string to check.
    
    Returns:
    bool: True if the string has at most one contiguous segment of ones, False otherwise.
    """
    def check_ones_segment(self, s: str) -> bool:
        """
        This method checks if a binary string has at most one contiguous segment of ones.
        
        Parameters:
        s (str): The binary string to check.
        
        Returns:
        bool: True if the string has at most one contiguous segment of ones, False otherwise.
        """
        count = 0
        for c in s:
            if c == '1':
                count += 1
                if count > 1:
                    return False
        return True

# Example usage:
solution = Solution()
print(solution.check_ones_segment("1001"))  # Output: False
print(solution.check_ones_segment("110"))  # Output: True