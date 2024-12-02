class StringMatching:
    """
    Given an array of string words, return all strings in words that is a substring of another word.
    You can return the answer in any order.
    
    A substring is a contiguous sequence of characters within a string.
    """
    def string_matching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            for other_word in words:
                if word != other_word and other_word in word:
                    result.append(word)
                    break
        return result