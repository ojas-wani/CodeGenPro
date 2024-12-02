"""
This is a solution to add a dot (.) as the thousands separator and return it in string format.

Example 1:
    Input: n = 987    Output: "987"

Example 2:
    Input: n = 1234    Output: "1.234"

Constraints:
    0 <= n <= 231 - 1
"""
class Solution:
    """
    This function takes an integer `n` as input, converts it to a string, and adds a dot (.) as the thousands separator.
    It then returns the result as a string.

    :param n: The integer to add a dot (.) as the thousands separator.
    :return: The integer with a dot (.) as the thousands separator as a string.
    """
    def thousand_separator(self, n: int) -> str:
        n_str = str(n)
        result = ""
        for i, char in enumerate(reversed(n_str)):
            if i % 3 == 0 and i != 0:
                result = "." + result
            result = char + result
        return "0" + result if n != 0 else "0"

# add a newline at the end