package com.leetcode.bank;
/**
 * 1716. Calculate Money in Leetcode Bank
 *
 * Hercy wants to save money for his first car. He puts money in the LeetCode bank
 * every day.
 *
 * He starts by putting in `$1` on Monday, the first day. Every day from Tuesday
 * to Sunday, he will put in `$1` more than the day before. On every subsequent
 * Monday, he will put in `$1` more than the **previous Monday**.
 *
 * Given `n`, return _the total amount of money he will have in the LeetCode bank
 * at the end of the_ `nth` _day_.
 *
 * @author Wanjo
 */
public class Solution {
    public int totalMoney(int n) {
        int total = 0;
        int week = 1;
        int dayOfWeek = 1;

        for (int i = 1; i <= n; i++) {
            total += dayOfWeek + week;
            if (dayOfWeek == 7) {
                dayOfWeek = 1;
                week++;
            } else {
                dayOfWeek++;
            }
        }

        return total;
    }
}