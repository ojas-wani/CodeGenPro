/**
 * This class provides a solution to find the count of numbers with an even number of digits.
 */
package com.illiumanu;

import java.util.Arrays;

public class Solution {

    /**
     * This method finds the count of numbers with an even number of digits.
     *
     * @param nums An array of integers.
     * @return The count of numbers with an even number of digits.
     */
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if (String.valueOf(num).length() % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {12, 345, 2, 6, 7896};
        Arrays.stream(solution.findNumbers(nums).toString()).forEach(System.out::println);
    }
}