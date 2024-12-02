class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Negative numbers are not palindromes
            return False
        reversed_x = 0
        original_x = x
        while x != 0:
            remainder = x % 10
            reversed_x = reversed_x * 10 + remainder
            x = x // 10
        return original_x == reversed_x