"""
Docstring explaining the problem and the solution.
"""
class CountOddNumbersInIntervalRange:
    """
    The class responsible for counting odd numbers in a given interval range.
    """

    def countOdds(self, low: int, high: int) -> int:
        """
        This method counts the number of odd numbers in the given interval range.
        
        Args:
        low (int): The lower bound of the interval.
        high (int): The upper bound of the interval.
        
        Returns:
        int: The count of odd numbers in the interval range.
        """
        return (high - low) // 2 + (1 + high % 2)

# Add a newline at the end of the file to fix the Flake8 issue.