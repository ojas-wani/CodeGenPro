package com.example;

import java.util.ArrayList;
import java.util.List;

/**
 * A class to solve the lucky numbers in a matrix problem.
 */
public class LuckyNumbers {
    /**
     * Finds all lucky numbers in a given matrix.
     * 
     * @param matrix the input matrix
     * @return a list of all lucky numbers in the matrix
     */
    public List<Integer> luckyNumbers(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        
        for (int i = 0; i < m; i++) {
            int min = matrix[i][0];
            int minCol = 0;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < min) {
                    min = matrix[i][j];
                    minCol = j;
                }
            }
            int maxRow = matrix[0][0];
            for (int j = 0; j < n; j++) {
                if (matrix[0][j] > maxRow) {
                    maxRow = matrix[0][j];
                }
            }
            if (matrix[i][minCol] == maxRow) {
                result.add(matrix[i][minCol]);
            }
        }
        return result;
    }
}