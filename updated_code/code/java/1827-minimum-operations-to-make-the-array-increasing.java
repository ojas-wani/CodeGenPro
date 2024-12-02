package com.issues;

import java.util.Arrays;

/**
 * This class contains a method `minOperations` to find the minimum number of operations needed to make an array strictly increasing.
 */
public class Solution {
    /**
     * This method takes an integer array `nums` as input and returns the minimum number of operations needed to make `nums` strictly increasing.
     * 
     * @param nums the input integer array
     * @return the minimum number of operations needed to make `nums` strictly increasing
     */
    public int minOperations(int[] nums) {
        Arrays.sort(nums); // sort the array
        int res = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                res += nums[i - 1] - nums[i] + 1; // calculate the increment needed to make the array strictly increasing
                nums[i] = nums[i - 1] + 1; // update the array
            }
        }
        return res;
    }
}