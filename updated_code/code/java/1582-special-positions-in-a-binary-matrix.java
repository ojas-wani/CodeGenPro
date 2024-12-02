package solution;

/**
 * Given an `m x n` binary matrix `mat`, return _the number of special positions
 * in_`mat` _.
 * 
 * A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other
 * elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).
 */
public class Solution {

    public int numSpecial(int[][] mat) {
        int count = 0;
        int m = mat.length;
        int n = mat[0].length;

        // Check each cell in the matrix
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Check if the current cell is 1
                if (mat[i][j] == 1) {
                    // Check if this row has any other 1s
                    boolean hasOtherOnes = false;
                    for (int k = 0; k < n; k++) {
                        if (k != j && mat[i][k] == 1) {
                            hasOtherOnes = true;
                            break;
                        }
                    }

                    // Check if this column has any other 1s
                    boolean hasOtherOnesInColumn = false;
                    for (int k = 0; k < m; k++) {
                        if (k != i && mat[k][j] == 1) {
                            hasOtherOnesInColumn = true;
                            break;
                        }
                    }

                    // If this cell is the only 1 in its row and column, increment the count
                    if (!hasOtherOnes && !hasOtherOnesInColumn) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}