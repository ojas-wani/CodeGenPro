from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        counter = Counter(words[0])
        
        for word in words[1:]:
            counter &= Counter(word)
            
        for char, count in counter.items():
            result.extend([char] * count)
            
        return result