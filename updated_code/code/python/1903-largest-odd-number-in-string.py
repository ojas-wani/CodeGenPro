class Solution:
    """
    This class is used to solve the problem of finding the largest odd number in a given string.
    """

    def largest_odd_number(self, num: str) -> str:
        """
        This method returns the largest-valued odd integer that is a non-empty substring of `num`, or an empty string if no odd integer exists.
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[i:]
        return ""