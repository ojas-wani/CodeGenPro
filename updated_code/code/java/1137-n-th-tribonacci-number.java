// Package declaration
package com.tribonacci;

// Class comment
/**
 * This class provides a method to calculate the n-th Tribonacci number.
 */
public class Tribonacci {

    // Method comment
    /**
     * This method calculates the n-th Tribonacci number.
     * 
     * @param n The index of the Tribonacci number to be calculated.
     * @return The n-th Tribonacci number.
     */
    public int tribonacci(int n) {
        if (n == 0) {
            return 0; // Braces added
        } else if (n == 1 || n == 2) {
            return 1; // Braces added
        } else {
            int[] dp = new int[n + 1]; // Made the variable name longer
            dp[0] = 0; // Braces added
            dp[1] = 1;
            dp[2] = 1;
            for (int i = 3; i <= n; i++) { // Braces added
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
            }
            return dp[n];
        }
    }
}