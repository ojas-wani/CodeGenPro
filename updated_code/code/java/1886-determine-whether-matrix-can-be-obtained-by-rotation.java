package com.leetcode;

import java.util.Arrays;

public class Solution {
    /**
     * Given two `n x n` binary matrices `mat` and `target`, return `true` _if it is
     * possible to make_`mat` _equal to_`target` _by **rotating** _`mat` _in
     * **90-degree increments** , or _`false` _otherwise._
     *
     * @param mat the given matrix
     * @param target the target matrix
     * @return whether it is possible to make `mat` equal to `target` by rotating `mat`
     */
    public boolean findRotation(int[][] mat, int[][] target) {
        for (int k = 0; k < 4; k++) {
            if (Arrays.deepEquals(mat, rotateMatrix(mat))) {
                return true;
            }
            mat = transposeMatrix(mat);
            if (k < 3) {
                mat = rotateMatrix(mat);
            }
        }
        return false;
    }

    /**
     * Rotate a given matrix 90 degrees clockwise.
     *
     * @param mat the given matrix
     * @return the rotated matrix
     */
    public int[][] rotateMatrix(int[][] mat) {
        int[][] rotated = new int[mat.length][mat[0].length];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                rotated[j][mat.length - 1 - i] = mat[i][j];
            }
        }
        return rotated;
    }

    /**
     * Transpose a given matrix.
     *
     * @param mat the given matrix
     * @return the transposed matrix
     */
    public int[][] transposeMatrix(int[][] mat) {
        int[][] transposed = new int[mat[0].length][mat.length];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                transposed[j][i] = mat[i][j];
            }
        }
        return transposed;
    }
}