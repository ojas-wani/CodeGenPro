class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
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