from typing import List

class ShuffleStringSolution:
    """
    This class provides a solution to the problem of shuffling a string based on given indices.
    """

    def shuffle_string(self, s: str, indices: List[int]) -> str:
        """
        This function shuffles the given string based on the given indices.

        Args:
        s (str): The input string to be shuffled.
        indices (List[int]): The list of indices that determine the order of the characters in the shuffled string.

        Returns:
        str: The shuffled string.
        """
        result = [''] * len(s)
        for i, index in enumerate(indices):
            result[index] = s[i]
        return ''.join(result)