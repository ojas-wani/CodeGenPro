package com.target.array;

import java.util.Arrays;

class Solution {
    /**
     * Creates a target array based on the given nums and index.
     *
     * @param nums the array of integers
     * @param index the array of indices
     * @return the target array
     */
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] target = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            target[index[i]] = nums[i];
        }
        return target;
    }
}