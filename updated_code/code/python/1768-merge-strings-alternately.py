class solution:
    """
    This class provides a method to merge two strings by adding letters in 
    alternating order, starting with `word1`. If a string is longer than 
    the other, append the additional letters onto the end of the merged 
    string.

    Parameters:
    word1 (str): The first input string.
    word2 (str): The second input string.

    Returns:
    str: The merged string.
    """

    def merge_alternately(self, word1: str, word2: str) -> str:
        """
        This method merges two strings by adding letters in alternating order, 
        starting with `word1`. If a string is longer than the other, append 
        the additional letters onto the end of the merged string.

        Parameters:
        word1 (str): The first input string.
        word2 (str): The second input string.

        Returns:
        str: The merged string.
        """
        result = ""  # Initialize an empty string to store the result.
        i, j = 0, 0  # Initialize two pointers for `word1` and `word2`.

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]  # Add the current character from `word1` to the result.
                i += 1
            if j < len(word2):
                result += word2[j]  # Add the current character from `word2` to the result.
                j += 1

        return result  # Return the merged string.