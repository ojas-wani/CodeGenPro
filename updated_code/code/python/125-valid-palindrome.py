class ValidPalindrome:
    """
    A class to validate if a given string is a palindrome.
    
    Description:
    A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.
    
    Given a string `s`, return `true` _if it is a **palindrome** , or _`false` otherwise_.
    """

    def is_palindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome.
        
        Removes all non-alphanumeric characters, converts to lowercase, and checks if the
        resulting string is equal to its reverse.
        
        Args:
        s (str): The input string to check.
        
        Returns:
        bool: True if the string is a palindrome, False otherwise.
        """
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]