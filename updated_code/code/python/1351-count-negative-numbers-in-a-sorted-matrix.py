import typing

class Solution:
    def count_negatives(self, grid: typing.List[typing.List[int]]) -> int:
        """
        Given a `m x n` matrix `grid` which is sorted in non-increasing order both
        row-wise and column-wise, return the number of **negative** numbers in `grid`.

        Example 1:
            Input: grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
            Output: 8
            Explanation: There are 8 negatives number in the matrix.

        Example 2:
            Input: grid = [[3, 2], [1, 0]]
            Output: 0

        Constraints:
            * `m == grid.length`
            * `n == grid[i].length`
            * `1 <= m, n <= 100`
            * `-100 <= grid[i][j] <= 100`

        Follow up: Could you find an `O(n + m)` solution?
        """
        m, n = len(grid), len(grid[0])
        i, j = 0, n-1
        count = 0
        while i < m and j >= 0:
            if grid[i][j] < 0:
                count += n - j
                i += 1
            else:
                j -= 1
        return count

# Final newline added