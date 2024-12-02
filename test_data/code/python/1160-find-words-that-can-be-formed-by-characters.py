from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_count = 0
        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= chars_count[char] for char in word_count):
                total_count += len(word)
        return total_count