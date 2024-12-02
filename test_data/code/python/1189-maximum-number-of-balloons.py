Python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {"b": 0, "a": 0, "l": 0, "o": 0}
        for char in text:
            if char in count:
                count[char] += 1
                
        min_count = float("inf")
        for char, c in count.items():
            if char == "b" or char == "a":
                min_count = min(min_count, c)
            elif char == "l":
                min_count = min(min_count, c // 2)
            elif char == "o":
                min_count = min(min_count, c // 2)
            else:
                min_count = min(min_count, c // 1)
                
        return min_count