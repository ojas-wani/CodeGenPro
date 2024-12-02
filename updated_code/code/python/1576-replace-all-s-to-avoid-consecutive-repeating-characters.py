class ReplaceConsecutiveRepeatingCharacters:
    """
    This class is used to replace all '?' characters in a string with lowercase letters
    such that the final string does not contain any consecutive repeating characters.

    Attributes:
        None

    Methods:
        modify_string(s): This method takes a string 's' as input and returns the modified string.
    """

    def modify_string(self, s: str) -> str:
        """
        This method takes a string 's' as input and returns the modified string.
        All '?' characters in the string are replaced with lowercase letters
        such that the final string does not contain any consecutive repeating characters.

        Args:
            s (str): The input string

        Returns:
            str: The modified string
        """
        result = list(s)
        for i, char in enumerate(result):
            if char == '?':
                # Replace '?' with the first lowercase letter that does not repeat consecutively
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if i > 0 and result[i - 1] == c:
                        continue
                    if i < len(result) - 1 and result[i + 1] == c:
                        continue
                    result[i] = c
                    break
        return ''.join(result)