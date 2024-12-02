class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_numerical_value(word: str) -> int:
            return int(''.join(str(ord(c) - ord('a')) for c in word))

        return get_numerical_value(firstWord) + get_numerical_value(secondWord) == get_numerical_value(targetWord)