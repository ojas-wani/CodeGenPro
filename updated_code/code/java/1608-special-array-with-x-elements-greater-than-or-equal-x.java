package com.example;

import java.util.Arrays;

/**
 * Class comments are required.
 */
public class Solution {
    /**
     * Public method and constructor comments are required.
     * @param nums
     * @return
     */
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        
        for (int i = nums.length; i > 0; i--) {
            if (i == nums.length - nums.length % 2) {
                if (i == nums.length || nums[i - 1] < i) {
                    return i;
                }
            }
        }
        
        return -1;
    }
}