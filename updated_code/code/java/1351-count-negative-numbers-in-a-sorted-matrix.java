// Package declaration
package com.example;

import java.util.Arrays;

/**
 * This class solves the problem of counting negative numbers in a sorted matrix.
 */
public class Solution {
    /**
     * This method counts the number of negative numbers in a sorted matrix.
     * 
     * @param grid the input matrix
     * @return the number of negative numbers in the matrix
     */
    public int countNegatives(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int row = grid.length;
        int col = grid[0].length;
        int count = 0;
        
        // Start from the top right corner and move diagonally down and left
        int i = 0, j = col - 1;
        while (i < row && j >= 0) {
            if (grid[i][j] < 0) {
                // If the current element is negative, move down and increment the count
                count += col - j;
                i++;
            } else {
                // If the current element is not negative, move left
                j--;
            }
        }
        
        return count;
    }
}