// Package declaration
package com.pascals_triangle;

// Class comment
/**
 * This class generates the first numRows of Pascal's triangle.
 */
public class Solution {
    // Constructor
    public Solution() {
    }

    // Method comment
    /**
     * Returns the first numRows of Pascal's triangle.
     *
     * @param numRows the number of rows to generate
     * @return the first numRows of Pascal's triangle
     */
    public List<List<Integer>> generate(int numRows) {
        // Check for invalid input
        if (numRows <= 0) {
            return new ArrayList<>();
        }

        // Initialize the result list
        List<List<Integer>> result = new ArrayList<>();

        // Generate each row of the triangle
        for (int i = 0; i < numRows; i++) {
            // Initialize a new row
            List<Integer> row = new ArrayList<>();

            // Add the first element (1) to the row
            row.add(1);

            // Add the middle elements to the row
            if (i > 0) {
                List<Integer> prevRow = result.get(i - 1);
                for (int j = 1; j < i; j++) {
                    row.add(prevRow.get(j - 1) + prevRow.get(j));
                }
            }

            // Add the last element (1) to the row
            row.add(1);

            // Add the row to the result list
            result.add(row);
        }

        return result;
    }
}