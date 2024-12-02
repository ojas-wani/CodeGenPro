class TruncateSentence:
    """
    Class for truncating a sentence.

    Attributes:
    None

    Methods:
    truncate_sentence: Truncates a sentence to the specified number of words.
    """

    def truncate_sentence(self, sentence: str, k: int) -> str:
        """
        Truncates a sentence to the specified number of words.

        Args:
        sentence (str): The input sentence.
        k (int): The number of words to truncate to.

        Returns:
        str: The truncated sentence.
        """
        words = sentence.split()
        return ' '.join(words[:k])