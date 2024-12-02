package com.climbstairs;

/**
 * This class solves the climbing stairs problem, where we need to find the number of 
 * distinct ways to climb a staircase with 'n' steps, where each step can be either 1 or 2 steps.
 */
public class ClimbingStairs {

    /**
     * This method finds the number of distinct ways to climb a staircase with 'n' steps.
     * 
     * @param n The number of steps in the staircase.
     * @return The number of distinct ways to climb the staircase.
     */
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }

        // Create an array to store the number of distinct ways to climb up to a certain step
        int[] ways = new int[n + 1];
        ways[1] = 1;
        ways[2] = 2;

        // Iterate through each step in the staircase
        for (int i = 3; i <= n; i++) {
            ways[i] = ways[i - 1] + ways[i - 2]; // The number of ways to climb to the current step is the sum of the ways to climb to the previous two steps
        }

        // Return the number of distinct ways to climb to the top of the staircase
        return ways[n];
    }

    public static void main(String[] args) {
        ClimbingStairs solution = new ClimbingStairs();
        System.out.println(solution.climbStairs(2)); // Output: 2
        System.out.println(solution.climbStairs(3)); // Output: 3
    }
}