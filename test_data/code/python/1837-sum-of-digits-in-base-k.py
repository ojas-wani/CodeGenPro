class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n > 0:
            n, remainder = divmod(n, k)
            res += remainder
        return res