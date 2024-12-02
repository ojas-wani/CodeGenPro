package com.example;

import java.util.HashMap;
import java.util.Map;

/**
 * Solution for the Two Sum problem.
 */
public class Solution {
    /**
     * Two Sum is a problem where given an array of integers `nums` and an integer `target`, 
     * return _indices of the two numbers such that they add up to`target`_.
     * 
     * @param nums an array of integers
     * @param target an integer
     * @return indices of the two numbers that add up to the target
     */
    public int[] twoSum(int[] nums, final int target) {
        // Use a HashMap to store the indices of the numbers we've seen so far
        final Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i]; // calculate the complement of the current number
            if (map.containsKey(complement)) {
                // If the complement is already in the map, return its index and the current index
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i); // put the current number and its index into the map
        }
        // If no two numbers add up to the target, return an empty array
        return new int[0];
    }
}