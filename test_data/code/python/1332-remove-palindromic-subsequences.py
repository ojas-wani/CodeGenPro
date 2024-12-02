Python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        while s and s != s[::-1]:
            s = s[:-1] if s[-1] == s[0] else s[:-1] if s[-1] != s[0] else s
        return 1 if s else 0