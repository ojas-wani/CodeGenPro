class Solution:
    """
    Description: Given an integer `x`, return `true` _if_`x` _is a_ _ **palindrome**_ _,
    and_`false` _otherwise_.

    Follow-up: Could you solve it without converting the integer to a string?
    """
    def is_palindrome(self, x: int) -> bool:
        """
        Check if the integer is a palindrome.

        Args:
        x (int): The input integer.

        Returns:
        bool: True if the integer is a palindrome, False otherwise.
        """
        if x < 0:  # Negative numbers are not palindromes
            return False
        reversed_x = 0
        original_x = x
        while x != 0:
            remainder = x % 10
            reversed_x = reversed_x * 10 + remainder
            x = x // 10
        return original_x == reversed_x


# Add a newline at the end of the file