package com.example;

/**
 * This class contains a method to find the minimum distance to the target element in an array.
 */
public class Solution {
    /**
     * This method finds the minimum distance to the target element in an array.
     * @param nums the input array
     * @param target the target element
     * @param start the start index
     * @return the minimum distance to the target element
     */
    public int getMinDistance(int[] nums, int target, int start) {
        int minDistance = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                minDistance = Math.min(minDistance, Math.abs(i - start));
            }
        }
        return minDistance;
    }
}