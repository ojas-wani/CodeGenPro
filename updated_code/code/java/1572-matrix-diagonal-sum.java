package com.example;

// Added package declaration
import java.util.Arrays;

/**
 * Class description: The class is used to calculate the sum of the diagonal elements in a square matrix.
 */
public class Solution {

    /**
     * Method description: This method calculates the sum of the matrix diagonals.
     * 
     * @param mat the square matrix
     * @return the sum of the diagonal elements
     */
    public int diagonalSum(int[][] mat) {
        int n = mat.length;
        int sum = 0;
        boolean isOdd = (n & 1) == 1; // Check if the matrix is odd-sized

        // Calculate the sum of the primary diagonal
        for (int i = 0; i < n; i++) {
            sum += mat[i][i];
        }

        // Calculate the sum of the secondary diagonal
        for (int i = 0; i < n; i++) {
            sum += mat[i][n - i - 1];
        }

        // If the matrix is odd-sized, subtract the middle element
        if (isOdd) {
            sum -= mat[n / 2][n / 2];
        }

        return sum;
    }
}