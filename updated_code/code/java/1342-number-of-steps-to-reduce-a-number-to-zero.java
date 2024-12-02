package com.example;

/**
 * This class solves the problem of finding the number of steps to reduce a number to zero.
 * @author Your Name
 */
public class Solution {
    /**
     * Returns the number of steps to reduce the given number to zero.
     * @param num the input number
     * @return the number of steps
     */
    public int numberOfSteps(int num) {
        int steps = 0;
        final int originalNum = num; // make num final to avoid reassignment
        while (num > 0) {
            if ((num & 1) == 0) { // check if num is even
                num /= 2;
            } else {
                num -= 1;
            }
            steps++;
        }
        return steps;
    }
}