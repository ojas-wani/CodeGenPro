package com.github.wanio;

import java.util.Arrays;

/**
 * This class contains a method to find the distance value between two integer arrays.
 */
public class Solution {
    /**
     * Finds the distance value between two integer arrays.
     * 
     * @param arr1 the first integer array
     * @param arr2 the second integer array
     * @param d the maximum distance between the elements
     * @return the distance value between the two arrays
     */
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int count = 0;
        // Use Arrays.binarySearch to improve the search efficiency
        Arrays.sort(arr2);
        for (int i : arr1) {
            // Search for the element in a sorted array using binary search
            int idx = Arrays.binarySearch(arr2, i);
            if (idx < 0) {
                idx = -idx - 1;
            }
            // Check if the element is not found or the distance is greater than d
            if (idx == 0 || Math.abs(i - arr2[idx - 1]) > d) {
                count++;
            }
        }
        return count;
    }
}