class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        digits = list(sorted(digits, reverse=True))
        if len(digits) < 2:
            return -1
        return digits[1]