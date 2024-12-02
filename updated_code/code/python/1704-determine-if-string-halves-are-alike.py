import string
import set

class HalvesAreAlike:
    """
    Determine if the halves of a given string are alike.

    A string is "alike" if it has the same number of vowels.
    """

    def __init__(self):
        """
        Initialize the solution.
        """

    def halves_are_alike(self, s: str) -> bool:
        """
        Determine if the halves of a given string are alike.

        Args:
        s (str): The input string.

        Returns:
        bool: Whether the halves of the string are alike.
        """

        vowels = set(string.ascii_lowercase + string.ascii_uppercase)
        
        half = len(s) // 2
        
        a = sum(1 for char in set(s[:half]).intersection(vowels))
        b = sum(1 for char in set(s[half:]).intersection(vowels))
        
        return a == b


# Test cases
solution = HalvesAreAlike()
print(solution.halves_are_alike("book"))  # True
print(solution.halves_are_alike("textbook"))  # False