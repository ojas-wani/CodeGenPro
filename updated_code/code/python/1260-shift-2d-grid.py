class ShiftGrid:
    """
    A 2D grid of size m x n and an integer k. You need to shift the grid k times.
    In one shift operation:
    * Element at grid[i][j] moves to grid[i][j + 1].
    * Element at grid[i][n - 1] moves to grid[i + 1][0].
    * Element at grid[m - 1][n - 1] moves to grid[0][0].
    Return the 2D grid after applying shift operation k times.
    """
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Shift grid k times.
        """
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        flat = [num for row in grid for num in row]
        flat = flat[-k:] + flat[:-k]
        rows = [list(x) for x in zip(*[iter(flat)] * n)]
        return rows