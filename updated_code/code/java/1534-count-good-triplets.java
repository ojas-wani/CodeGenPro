package com.codequality;

import java.util.Arrays;

/**
 * This class counts the number of good triplets in an array.
 */
public class Solution {
    /**
     * Counts the number of good triplets in the array.
     * 
     * @param arr     the input array of integers
     * @param a       the first condition
     * @param b       the second condition
     * @param c       the third condition
     * @return the number of good triplets
     */
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                for (int k = j + 1; k < arr.length; k++) {
                    if (Math.abs(arr[i] - arr[j]) <= a && Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}