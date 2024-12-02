class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 0
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            max_power = max(max_power, count)
            i += 1
        return max_power