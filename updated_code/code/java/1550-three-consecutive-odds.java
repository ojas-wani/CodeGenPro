package com.example;

import java.util.Arrays;

/**
 * This class solves the problem of finding three consecutive odd numbers in an array.
 */
public class Solution {

    /**
     * This method checks if there are three consecutive odd numbers in the array.
     * @param arr the input array
     * @return true if there are three consecutive odd numbers, false otherwise
     */
    public boolean threeConsecutiveOdds(int[] arr) {
        for (int i = 0; i < arr.length - 2; i++) {
            if (arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0) {
                return true;
            }
        }
        return false;
    }
}