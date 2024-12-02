package code;

public class Solution {
    /**
     * You are given an array prices where prices[i] is the price of a given stock on the ith day.
     * 
     * You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
     * 
     * Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.
     * 
     * @param prices an array of stock prices
     * @return the maximum profit that can be achieved from a single transaction
     */
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        for(int i = 1; i < prices.length; i++) {
            // Avoid buying at a price that is higher than what we already have
            if(prices[i] < minPrice) {
                minPrice = prices[i];
            } else if(prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
        }

        return maxProfit;
    }
}