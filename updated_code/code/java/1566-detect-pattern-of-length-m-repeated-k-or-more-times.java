package com.example;

import java.util.Arrays;

/**
 * This class contains the solution to the problem 
 * Detect Pattern of Length M Repeated K or More Times.
 */
public class Solution {
    /**
     * A method that checks if there exists a pattern of length `m` 
     * that is repeated `k` or more times in the given array `arr`.
     * 
     * @param arr  an array of positive integers
     * @param m    the length of the pattern
     * @param k    the number of times the pattern is repeated
     * @return     true if the pattern is found, otherwise false
     */
    public boolean containsPattern(int[] arr, int m, int k) {
        if (arr.length < m * k) return false;
        
        // Check if there is a pattern of length `m` that is repeated `k` or more times
        for (int i = 0; i <= arr.length - m * k; i++) {
            if (i + m - 1 < arr.length && Arrays.equals(Arrays.copyOfRange(arr, i, i + m), Arrays.copyOfRange(arr, i + m, i + m * k))) {
                return true;
            }
        }
        return false;
    }
}