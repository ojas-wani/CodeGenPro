package code;

import java.util.Arrays;

class Solution {
    /**
     * Class to solve the problem of counting the number of rectangles that can form the largest square.
     */
    public int countGoodRectangles(int[][] rectangles) {
        /**
         * Method to count the number of rectangles that can form the largest square.
         * 
         * @param rectangles an array where each rectangle is represented by an array of two integers, 
         *                    specifying the length and width of the rectangle.
         * @return the number of rectangles that can form a square with a side length equal to maxLen.
         */
        int maxLen = 0, count = 0;
        for (int[] rectangle : rectangles) {
            /**
             * Calculate the smallest side length of the rectangle.
             */
            int length = Math.min(rectangle[0], rectangle[1]);
            if (length > maxLen) {
                // Update maxLen and reset count if a larger side length is found
                maxLen = length;
                count = 1;
            } else if (length == maxLen) {
                // Increment count for rectangles with a side length equal to maxLen
                count++;
            }
        }
        return count;
    }
}