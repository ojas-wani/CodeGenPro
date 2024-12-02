class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence += ' '
        word_index = 0
        for i, c in enumerate(sentence):
            if c == ' ':
                word_index += 1
                if i > 0 and sentence[i-1:i] == searchWord:
                    return word_index
        return -1