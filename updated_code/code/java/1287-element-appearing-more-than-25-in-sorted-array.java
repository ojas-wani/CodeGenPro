/**
 * This class is used to find the element that appears more than 25% of the time in a sorted array.
 */
package com.example.problem1287;

public class Solution {

    /**
     * This method finds the element that appears more than 25% of the time in a sorted array.
     * 
     * @param arr the input array
     * @return the element that appears more than 25% of the time
     */
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        final int targetCount = (int) Math.ceil(n * 0.25);
        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = i + 1; j < n; j++) {
                if (arr[i] == arr[j]) {
                    count++;
                } else {
                    break;
                }
            }
            if (count >= targetCount) {
                return arr[i];
            }
        }
        return -1;
    }
}