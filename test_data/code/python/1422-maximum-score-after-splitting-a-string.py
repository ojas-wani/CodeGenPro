Python
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_zeros = sum(1 for c in s if c == '0')
        max_score = 0
        left_zeros = 0
        for right_zero in range(n):
            left_zeros += 1 if s[right_zero] == '0' else 0
            max_score = max(max_score, left_zeros + total_zeros - left_zeros)
        return max_score