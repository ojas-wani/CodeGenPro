package com.lessons;

import java.util.Locale;

public class Solution {
    /**
     * A phrase is a palindrome if, after converting all uppercase letters into
     * lowercase letters and removing all non-alphanumeric characters, it reads
     * the same forward and backward. Alphanumeric characters include letters
     * and numbers.
     * 
     * @param s the input string
     * @return true if the string is a palindrome, or false otherwise
     */
    public boolean isPalindrome(String s) {
        // Convert all letters to lowercase and remove non-alphanumeric characters
        String cleanS = s.replaceAll("[^a-zA-Z0-9]+", "").toLowerCase(Locale.US);

        // Initialize two pointers, one at the start and one at the end of the string
        int start = 0;
        int end = cleanS.length() - 1;

        // Compare characters from both ends until they meet
        while (start < end) {
            // If the characters at the start and end do not match, return false
            if (cleanS.charAt(start) != cleanS.charAt(end)) {
                return false;
            }
            // Move the pointers closer to the center of the string
            start++;
            end--;
        }
        // If the loop finishes without finding a mismatch, the string is a palindrome
        return true;
    }
}