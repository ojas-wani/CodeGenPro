package com.solution;

import java.util.Scanner;

/**
 * Improved Code Quality for Solution Class
 */
public class Solution {

    /**
     * Split a string into balanced strings
     *
     * @param s The input string
     * @return The maximum number of balanced strings
     */
    public int balancedStringSplit(String s) {
        int count = 0;
        int balance = 0;
        final char LEFT = 'L';
        final char RIGHT = 'R';

        for (char c : s.toCharArray()) {
            // Use constants for easier reading
            if (c == LEFT) {
                balance--;
            } else if (c == RIGHT) {
                balance++;
            }
            // Check if the balance is zero
            if (balance == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution solution = new Solution();
        System.out.println("Enter the string: ");
        String s = scanner.nextLine();
        System.out.println("Number of balanced strings: " + solution.balancedStringSplit(s));
    }
}