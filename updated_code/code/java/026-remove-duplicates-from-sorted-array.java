package com.question;

import java.util.Arrays;

/**
 * Remove Duplicates from Sorted Array
 *
 * @author WaniO
 */
public class Solution {
    /**
     * Removes duplicates in-place and returns the length of the unique elements.
     *
     * @param nums an integer array sorted in non-decreasing order
     * @return the number of unique elements
     */
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        
        int i = 0; // initialize a pointer to track the last unique element
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++; // move the pointer if a new unique element is found
                nums[i] = nums[j]; // assign the new unique element to the pointer's position
            }
        }
        
        return i + 1; // return the number of unique elements
    }
}