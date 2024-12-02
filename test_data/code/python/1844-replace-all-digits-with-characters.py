class Solution:
    def replaceDigits(self, s: str) -> str:
        result = list(s)
        for i in range(1, len(s), 2):
            prev, curr = result[i - 1], result[i]
            result[i] = chr(ord(prev) + int(curr))
        return ''.join(result)