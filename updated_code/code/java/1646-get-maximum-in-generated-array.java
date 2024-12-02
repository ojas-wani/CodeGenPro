package com.example;
/**
* This is a class that generates an array based on given rules and finds the maximum element in the array.
*
* @author Your Name
*/
public class Solution {
    /**
    * This method generates an array based on given rules and finds the maximum element in the array.
    *
    * @param n the input integer
    * @return the maximum integer in the array
    */
    public int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        int[] nums = new int[n + 1];
        nums[0] = 0;
        nums[1] = 1;
        int max = 1;
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                nums[i] = nums[i / 2];
            } else {
                nums[i] = nums[i / 2] + nums[i / 2 + 1];
            }
            max = Math.max(max, nums[i]);
        }
        return max;
    }
}