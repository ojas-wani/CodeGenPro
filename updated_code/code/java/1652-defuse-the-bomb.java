package com.code.java;

import java.util.Arrays;

public class Solution {

    public int[] decrypt(int[] code, int k) {
        if (code == null || code.length == 0) {
            return new int[0];
        }

        int n = code.length;
        int[] result = new int[n];
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum = 0;
            for (int j = 1; j <= Math.abs(k); j++) {
                int index = (i + j - 1) % n;
                sum += code[index];
            }
            result[i] = k > 0 ? sum : -sum;
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] code = {5, 7, 1, 4};
        int k = 3;
        int[] result = solution.decrypt(code, k);
        System.out.println(Arrays.toString(result));
    }
}