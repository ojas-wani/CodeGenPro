package com.code.lemoshowman;

import java.util.*;

/**
 * Class comments are required
 */
public class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        // Public method and constructor comments are required
        Arrays.sort(nums);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], i);
            }
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = map.getOrDefault(nums[i] - 1, -1);
        }
        return result;
    }
}