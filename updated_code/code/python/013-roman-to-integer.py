class RomanToInt:
    """
    This class is used to convert roman numerals to integers.
    """

    def __init__(self):
        """
        This function initializes the class.
        """

    def roman_to_int(self, s: str) -> int:
        """
        This function converts a roman numeral to an integer.

        Args:
        s (str): The roman numeral to be converted.

        Returns:
        int: The integer value of the roman numeral.
        """
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i, char in enumerate(s):
            if i > 0 and roman_to_int[char] > roman_to_int[s[i - 1]]:
                res += roman_to_int[char] - 2 * roman_to_int[s[i - 1]]
            else:
                res += roman_to_int[char]
        return res