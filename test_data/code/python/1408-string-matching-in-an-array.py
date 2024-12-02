Python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for other_word in words:
                if word != other_word and other_word in word:
                    result.append(word)
                    break
        return result