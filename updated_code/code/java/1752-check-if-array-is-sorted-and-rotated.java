package problem1752;

import java.util.Arrays;

class Solution {
    public boolean check(int[] nums) {
        // Check if the array is not rotated and still sorted in non-decreasing order
        if (Arrays.stream(nums).distinct().count() == 1) {
            Arrays.sort(nums);
            return Arrays.equals(nums, nums.clone()); // Check if the array is sorted
        }

        // Check if the array was rotated some number of positions
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                // Check if the array was rotated with the smallest element as the pivot
                if (i == 0 || nums[i] < nums[i - 1]) {
                    return true;
                } else {
                    return false;
                }
            }
        }
        return nums[0] <= nums[nums.length - 1];
    }
}