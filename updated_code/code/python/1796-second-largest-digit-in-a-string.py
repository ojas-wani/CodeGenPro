"""
Description:
Given an alphanumeric string s, return the **second largest** numerical digit that appears in s, or -1 if it does not exist.

Example 1:
Input: s = "dfa12321afd"    Output: 2    Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"    Output: -1    Explanation: The digits that appear in s are [1]. There is no second largest digit.

Constraints:
* 1 <= s.length <= 500
* s consists of only lowercase English letters and/or digits.
"""
class SecondHighestDigitSolutions(object):
    """
    This class contains a method to find the second highest numerical digit in a string.
    """
    def second_highest(self, s: str) -> int:
        """
        This method returns the second highest numerical digit in a string, or -1 if it does not exist.
        
        Args:
        s (str): An alphanumeric string.
        
        Returns:
        int: The second highest numerical digit in the string, or -1 if it does not exist.
        """
        # Convert the string to a set of digits to remove duplicates
        digits = set(c for c in s if c.isdigit())
        
        # Convert the set of digits to a list and sort it in descending order
        sorted_digits = sorted(map(int, digits), reverse=True)
        
        # If the list of digits contains less than 2 elements, return -1
        if len(sorted_digits) < 2:
            return -1
        else:
            # Otherwise, return the second highest digit
            return sorted_digits[1]