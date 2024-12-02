package com. solutions;

/**
 * This class provides a solution for the arraySign problem.
 *
 * @author yourname
 */
public class Solution {

    /**
     * This method calculates the sign of the product of all values in an array.
     *
     * @param nums an integer array
     * @return the sign of the product of all values in the array
     */
    public int arraySign(int[] nums) {
        int sign = 1;
        for (final int num : nums) {
            if (num == 0) {
                return 0;
            }
            final boolean isNegative = num < 0;
            sign = isNegative ? -sign : sign;
        }
        return sign;
    }
}