package com.leetcode;

import java.util.Arrays;

public class Solution {
    /**
     * Sorts the integers in the array in ascending order by the number of '1's in their binary representation
     * and in case of two or more integers have the same number of '1's, sorts them in ascending order.
     *
     * @param arr the input array
     * @return the array after sorting
     */
    public int[] sortByBits(int[] arr) {
        int[] result = new int[arr.length];
        System.arraycopy(arr, 0, result, 0, arr.length);
        Arrays.sort(result, (a, b) -> {
            int oneCountA = Integer.bitCount(a);
            int oneCountB = Integer.bitCount(b);
            if (oneCountA != oneCountB) {
                return Integer.compare(oneCountA, oneCountB);
            } else {
                return Integer.compare(a, b);
            }
        });
        return result;
    }
}