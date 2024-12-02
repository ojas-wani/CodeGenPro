package com.lloyd;

/**
 * This class provides a method to replace elements in an array with the greatest
 * element among the elements to its right, and replace the last element with -1.
 *
 * @author Lloyd
 */
public class Solution {

    /**
     * Replaces every element in the given array with the greatest element among
     * the elements to its right, and replaces the last element with -1.
     *
     * @param arr The input array
     * @return The modified array
     */
    public int[] replaceElements(int[] arr) {
        int n = arr.length;
        if (n == 0) {
            return new int[0];
        }

        int max = arr[n - 1];
        arr[n - 1] = -1;

        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > max) {
                max = arr[i];
            }
            arr[i] = max;
        }

        return arr;
    }
}