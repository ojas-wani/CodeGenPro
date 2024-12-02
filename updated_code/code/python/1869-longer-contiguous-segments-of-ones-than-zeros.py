__author__ = "Author's Name"
__version__ = "1.0"

class Solution:
    """
    This class solves the problem of finding the longest contiguous segment of 1's
    in a binary string and comparing it with the longest contiguous segment of 0's.
    """

    def longest_continuous_segment(self, s: str, max_len: int) -> int:
        """
        This function calculates the length of the longest contiguous segment in the string.
        """
        current_len = 0
        max_len = max_len
        for char in s:
            if char == '1':
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        return max_len

    def checkZeroOnes(self, s: str) -> bool:
        ones_len = self.longest_continuous_segment(s, 0)
        zeros_len = self.longest_continuous_segment(s, 0)
        return ones_len > zeros_len