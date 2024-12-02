from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Given an integer `n`, return a list of two integers `[a, b]` where:
        * `a` and `b` are No-Zero integers.
        * `a + b = n`

        The test cases are generated so that there is at least one valid solution.
        If there are many valid solutions, you can return any of them.
        """
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]