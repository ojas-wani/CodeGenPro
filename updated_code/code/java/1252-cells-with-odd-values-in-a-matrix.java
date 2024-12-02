// Package declaration
package com.example;

import java.util.Arrays;

// Class declaration
public class CellsWithOddValuesInAMatrix {
    public int oddCells(int rows, int cols, int[][] indices) {
        int[] rowCounts = new int[rows];
        int[] colCounts = new int[cols];

        // Increment all cells on each row and column
        for (int[] index : indices) {
            int row = index[0];
            int col = index[1];
            rowCounts[row]++;
            colCounts[col]++;
        }

        int oddCells = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int cell = rowCounts[i] + colCounts[j];
                if (cell % 2 != 0) {
                    oddCells++;
                }
            }
        }

        return oddCells;
    }
}

public class Solution {
    public int oddCells(int rows, int cols, int[][] indices) {
        int[][] matrix = new int[rows][cols];
        int count = 0;

        int[] rowCounts = new int[rows];
        int[] colCounts = new int[cols];

        for (int[] index : indices) {
            int row = index[0];
            int col = index[1];
            rowCounts[row]++;
            colCounts[col]++;
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int cell = rowCounts[i] + colCounts[j];
                if (cell % 2 != 0) {
                    count++;
                }
            }
        }

        return count;
    }
}