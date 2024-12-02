class Solution:
    """
    This class defines a method to find the maximum number that can be formed
    by changing at most one digit in the given integer.
    """
    def maximum_69_number(self, num: int) -> int:
        """
        This method takes an integer num as input and returns the maximum number
        that can be formed by changing at most one digit.
        """
        num = str(num)
        for i, c in enumerate(num):  # Use enumerate instead of range and len
            if c == '6':
                return int(num[:i] + '9' + num[i+1:])
        return num