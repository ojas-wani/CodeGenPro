package com.correct.packagename;

/**
 * This is a class that solves the problem of making two arrays equal by reversing subarrays.
 */
public class Solution {

    /**
     * This method checks if it is possible to make arr equal to target by reversing subarrays.
     * 
     * @param target the target array
     * @param arr the array to be modified
     * @return true if it is possible to make arr equal to target, false otherwise
     */
    public boolean canBeEqual(int[] target, final int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < target.length; i++) {
            map.put(target[i], map.getOrDefault(target[i], 0) + 1);
            map.put(arr[i], map.getOrDefault(arr[i], 0) - 1);
        }
        final int count;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            count = entry.getValue();
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
}