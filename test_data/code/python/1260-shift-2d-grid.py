Python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        flat = [num for row in grid for num in row]
        flat = flat[-k:] + flat[:-k]
        rows = [list(x) for x in zip(*[iter(flat)] * n)]
        return rows