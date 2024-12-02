package com.leetcode;

import java.util.Arrays;

class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        boolean[] used = new boolean[pieces.length];
        for (int[] piece : pieces) {
            boolean formed = true;
            for (int i = 0; i < arr.length; ) {
                if (Arrays.equals(Arrays.copyOfRange(arr, i, i + piece.length), piece)) {
                    i += piece.length;
                } else {
                    formed = false;
                    break;
                }
            }
            if (!formed) {
                return false;
            }
        }
        return true;
    }
}