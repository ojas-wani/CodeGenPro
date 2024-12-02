class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        for (int k = 0; k < 4; k++) {
            if (Arrays.deepEquals(mat, rotateArray(mat))) {
                return true;
            }
            mat = transpose(mat);
            if (k < 3) {
                mat = rotateArray(mat);
            }
        }
        return false;
    }

    public int[][] rotateArray(int[][] mat) {
        int[][] rotated = new int[mat.length][mat[0].length];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                rotated[j][mat.length - 1 - i] = mat[i][j];
            }
        }
        return rotated;
    }

    public int[][] transpose(int[][] mat) {
        int[][] transposed = new int[mat[0].length][mat.length];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                transposed[j][i] = mat[i][j];
            }
        }
        return transposed;
    }
}