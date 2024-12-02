package com.example;

import java.util.Arrays;

/**
 * This class provides a solution to increment a large integer represented as an integer array by one.
 */
public class Solution {

    /**
     * Increments the large integer represented as an integer array by one and returns the resulting array of digits.
     * 
     * @param digits The large integer represented as an integer array.
     * @return The resulting array of digits after incrementing the large integer by one.
     */
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }
        // Create a new array with one more element to store the incremented value
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1;
        // Copy the remaining elements to the new array
        System.arraycopy(digits, 0, newDigits, 1, n);
        return newDigits;
    }
}