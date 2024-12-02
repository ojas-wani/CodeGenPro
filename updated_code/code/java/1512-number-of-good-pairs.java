package com.lloydcode.quality;

/**
 * Solution for the "Number of Good Pairs" problem.
 */
public class Solution {

    /**
     * Returns the number of good pairs in the given array of integers.
     * 
     * @param nums an array of integers
     * @return the number of good pairs
     */
    public int numIdenticalPairs(int[] nums) {
        int count = 0;
        final Map<Integer, Integer> map = new HashMap<>();
        int num;
        for (int i = 0; i < nums.length; i++) {
            num = nums[i];
            if (map.containsKey(num)) {
                count += map.get(num);
            }
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        return count;
    }
}