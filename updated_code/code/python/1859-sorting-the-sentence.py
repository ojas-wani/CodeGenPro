import re

class SortingSentence:
    """
    A class to solve sorting sentence problems.
    """
    def __init__(self):
        """Class constructor."""
        pass

    def sort_sentence(self, sentence: str) -> str:
        """
        Reconstruct and return the original sentence.

        Parameters:
        s (str): A shuffled sentence.

        Returns:
        str: The original sentence.
        """
        words = ["" for _ in range(9)]
        temp = list(sentence.split(' '))

        for word in temp:
            index = int(re.search(r'\d+', word).group())
            words[index - 1] = word.replace(str(index), '')
            temp.remove(word)

        # Remove trailing space, join and return
        return ' '.join(map(str.strip, words)).strip()