package com.wwgjavaprogrammer;

import java.util.Arrays;

/**
 * Merge two sorted arrays into one sorted array.
 */
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Set pointers for nums1 and nums2 from end
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        // Merge from end to start
        while (i >= 0 || j >= 0) {
            if (i >= 0 && j >= 0) {
                if (nums1[i] > nums2[j]) {
                    nums1[k--] = nums1[i--];
                } else {
                    nums1[k--] = nums2[j--];
                }
            } else if (i >= 0) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
}