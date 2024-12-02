Python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # remove leading and trailing spaces
        words = s.split()  # split the string into a list of words
        return len(words[-1])  # return the length of the last word