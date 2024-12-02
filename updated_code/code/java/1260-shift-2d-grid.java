import java.util.ArrayList;
import java.util.List;

public class Solution {
    /**
     * Shift the given 2D grid to the right by k times.
     * 
     * @param grid   The 2D grid to be shifted
     * @param k      The number of times to shift the grid
     * @return The shifted 2D grid
     */
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        if (grid == null || grid.length == 0) {
            return new ArrayList<>();
        }

        int m = grid.length; // number of rows
        int n = grid[0].length; // number of columns
        k = k % (m * n); // prevent overflow

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(grid[i][j]);
            }
            result.add(row);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int index = (i * n + j + k) % (m * n);
                result.get(index / n).set(index % n, grid[i][j]);
            }
        }

        return result;
    }
}