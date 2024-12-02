Python
class Solution:
    def totalMoney(self, n: int) -> int:
        n -= 1     # subtract 1 because Monday is 0
        week = n // 7
        remainder = n % 7
        return week * 28 + sum(range(1, 8)) + sum(range(1, remainder + 1))