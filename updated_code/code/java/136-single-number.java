package com.example;

/**
 * This class provides a solution to the problem of finding a single number that appears only once in a non-empty array of integers, where every element appears twice except for one.
 */
public class SingleNumber {

    /**
     * Method to find the single number in an array of integers.
     *
     * @param nums a non-empty array of integers, where every element appears twice except for one.
     * @return the single number that appears only once in the array.
     */
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
}