Python
class Solution:
    """
    This class is used to solve the problem of decrypting a string based on the alphabet-to-integer mapping.

    Attributes:
    None

    Methods:
    freqAlphabets(s: str) -> str: 
        This method decrypts the given string based on the alphabet-to-integer mapping.
        It returns the decrypted string.
    """
    def freqAlphabets(self, s: str) -> str:
        """
        This method decrypts the given string based on the alphabet-to-integer mapping.

        Args:
        s (str): The input string.

        Returns:
        str: The decrypted string.
        """
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                result.append(chr(int(s[i:i+3]) + 96))
                i += 3
            else:
                result.append(chr(int(s[i]) + 96))
                i += 1
        return ''.join(result)