package com.example;

import java.util.ArrayList;
import java.util.List;

/**
 * Description: Given an array of positive integers `nums`, return the _maximum possible sum
 *              of an **ascending** subarray in _`nums`.
 *
 * @author {Your Name}
 * @version 1.0
 * @since 2022-01-01
 */
public class Solution {
    /**
     * This method calculates the maximum ascending subarray sum.
     *
     * @param nums The input array of positive integers.
     * @return The maximum possible sum of an ascending subarray in `nums`.
     */
    public int maxAscendingSum(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];
        
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] > nums[i - 1]) {
                currentSum += nums[i];
            } else {
                maxSum = Math.max(maxSum, currentSum);
                currentSum = nums[i];
            }
        }
        
        return Math.max(maxSum, currentSum);
    }
}