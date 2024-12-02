Python
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxOnes = 0
        maxZeros = 0
        currentOnes = 0
        currentZeros = 0

        for char in s:
            if char == '1':
                currentOnes += 1
                maxOnes = max(maxOnes, currentOnes)
                currentZeros = 0
            else:
                currentZeros += 1
                maxZeros = max(maxZeros, currentZeros)
                currentOnes = 0

        return maxOnes > maxZeros