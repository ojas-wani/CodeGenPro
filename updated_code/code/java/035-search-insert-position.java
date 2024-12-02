package com.example.searchinsert;

import java.util.Arrays;

public class Solution {
    /**
     * Returns the index where the target is found. If not, returns the index
     * where it would be if it were inserted in order.
     * 
     * @param nums   a sorted array of distinct integers
     * @param target the target value
     * @return the index where the target is found or where it would be if inserted
     */
    public int searchInsert(int[] nums, int target) {
        // Initialize two pointers for binary search
        int left = 0, right = nums.length - 1;

        // Perform binary search
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If the target is found, return the index
            if (nums[mid] == target) {
                return mid;
            }
            // If the target is less than the middle element, move the right pointer
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            // If the target is greater than the middle element, move the left pointer
            else {
                right = mid - 1;
            }
        }

        // If the target is not found, return the left pointer
        return left;
    }
}