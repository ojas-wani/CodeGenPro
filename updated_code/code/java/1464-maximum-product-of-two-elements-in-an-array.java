/**
 * This class provides a method to calculate the maximum product of two elements in an array.
 */
package com.example.leetcode;

import java.util.Arrays;

public class Solution {
    /**
     * This method calculates the maximum product of two elements in an array.
     * @param nums an array of integers
     * @return the maximum value of (nums[i]-1)*(nums[j]-1)
     */
    public int maxProduct(int[] nums) {
        // Sort the array in descending order
        Arrays.sort(nums);
        // Calculate the maximum product of two elements
        return (nums[nums.length-1] - 1) * (nums[nums.length-2] - 1);
    }
}