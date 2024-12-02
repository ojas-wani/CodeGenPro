Python
class Solution:
    """
    This class is used to solve the problem of finding the maximum score after
    splitting a string into two non-empty substrings.

    Attributes:
    None

    Methods:
    maxScore(s): This method calculates the maximum score after splitting the
    string 's' into two non-empty substrings.

    Returns:
    The maximum score.
    """

    def maxScore(self, s: str) -> int:
        """
        This method calculates the maximum score after splitting the string 's'
        into two non-empty substrings.

        Args:
        s (str): The input string.

        Returns:
        The maximum score.
        """
        total_zeros = sum(1 for c in s if c == '0')
        max_score = 0
        left_zeros = 0
        for right_zero in range(len(s)):  # Use len() function to get the length of the string
            left_zeros += 1 if s[right_zero] == '0' else 0
            max_score = max(max_score, left_zeros + total_zeros - left_zeros)
        return max_score