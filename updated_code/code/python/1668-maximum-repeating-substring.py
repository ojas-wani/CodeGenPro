class MaximumRepeating:
    """
    This class provides a method to find the maximum repeating value of a word in a sequence.
    """

    def __init__(self):
        """
        This is the constructor of the class.
        """

    def max_repeating(self, sequence: str, word: str) -> int:
        """
        This method finds the maximum repeating value of a word in a sequence.

        Args:
        sequence (str): The input sequence.
        word (str): The word to find the maximum repeating value for.

        Returns:
        int: The maximum repeating value of the word in the sequence.
        """
        max_k = 0
        for k in range(1, len(sequence) // len(word) + 1):
            if sequence.replace(word * k, '', 1) == '':
                max_k = k
        return max_k