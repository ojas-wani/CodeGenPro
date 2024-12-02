class Solution:
    """
    This function calculates the maximum number of "balloon" strings that can be formed
    from the characters in the given text.
    
    :param text: The input string
    :return: The maximum number of "balloon" strings that can be formed
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {"b": 0, "a": 0, "l": 0, "o": 0}
        for char in text:
            if char in count:
                count[char] += 1
                
        min_count = float("inf")
        for char, count_val in count.items():
            if char == "b" or char == "a":
                min_count = min(min_count, count_val)
            elif char == "l":
                min_count = min(min_count, count_val // 2)
            elif char == "o":
                min_count = min(min_count, count_val // 2)
            else:
                min_count = min(min_count, count_val)
                
        return min_count