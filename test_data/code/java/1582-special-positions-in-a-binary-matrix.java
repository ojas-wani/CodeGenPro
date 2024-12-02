class Solution {
    public int numSpecial(int[][] mat) {
        int count = 0;
        for (int i = 0; i < mat.length; i++) {
            boolean rowHasOne = false;
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 1) {
                    rowHasOne = true;
                }
            }
            if (rowHasOne) {
                boolean colHasOne = false;
                for (int j = 0; j < mat[i].length; j++) {
                    if (mat[j][i] == 1 && j != i) {
                        colHasOne = true;
                        break;
                    }
                }
                if (!colHasOne) {
                    count++;
                }
            }
        }
        return count;
    }
}