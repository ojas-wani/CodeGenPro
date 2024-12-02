package com.example;

import java.util.Arrays;

public class Solution {
    /**
     * Decompresses a run-length encoded list.
     *
     * @param nums the run-length encoded list
     * @return the decompressed list
     */
    public int[] decompressRLElist(int[] nums) {
        int n = nums.length;
        int[] res = new int[n / 2];
        for (int i = 0; i < n; i += 2) {
            for (int j = 0; j < nums[i]; j++) {
                res[i / 2 + j] = nums[i + 1];
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[] {1, 2, 3, 4};
        int[] result = solution.decompressRLElist(nums);
        System.out.println(Arrays.toString(result)); // [2, 4, 4, 4]
    }
}