package com.solution;

import java.util.Arrays;

/**
 * Shuffle the array
 */
public class Solution {

    /**
     * Shuffle the array
     * 
     * @param nums an array consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]
     * @param n    the number of elements in the first half of the array
     * @return the array in the form [x1,y1,x2,y2,...,xn,yn]
     */
    public int[] shuffle(int[] nums, final int n) {
        final int[] result = new int[nums.length];
        for (int i = 0; i < n; i++) {
            System.arraycopy(nums, i, result, 2 * i, 1);
            System.arraycopy(nums, n + i, result, 2 * i + 1, 1);
        }
        return result;
    }
}