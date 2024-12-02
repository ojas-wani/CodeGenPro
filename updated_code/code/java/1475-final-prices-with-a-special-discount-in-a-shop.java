package com.leetcode;
/**
 * Your Solution class should implement the Solution interface.
 */
public class Solution {
    public int[] finalPrices(int[] prices) {
        int[] res = new int[prices.length];
        res = prices.clone(); // Make a copy of the original array
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                if (prices[j] <= prices[i]) {
                    res[i] -= prices[j];
                    break;
                }
            }
        }
        return res;
    }
}