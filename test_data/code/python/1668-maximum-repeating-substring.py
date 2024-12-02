Python
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_k = 0
        for k in range(1, len(sequence) // len(word) + 1):
            if sequence.replace(word * k, '', 1) == '':
                max_k = k
        return max_k