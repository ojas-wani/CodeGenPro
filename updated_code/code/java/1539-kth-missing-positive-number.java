package com.leetcode;

import java.util.Arrays;

public class Solution {
    public int findKthPositive(int[] arr, int k) {
        // Initialize two pointers, one at the start of the array and one at the first number
        int left = 0;
        int right = 1;

        // Loop through the array
        while (left < arr.length) {
            // Check how many numbers are missing from the array at this point
            while (right < arr[left] - 1) {
                k--;
                if (k == 0) {
                    return right;
                }
                right++;
            }
            left++;
        }

        // If there are remaining missing numbers, return those
        while (k > 0) {
            k--;
            right++;
        }

        return right;
    }
}