package com.issues.resolver;

/**
 * This is the Solution class that generates a string with `n` characters such that each character in such string occurs **an odd number of times**.
 */
public class Solution {
    /**
     * This method generates a string with `n` characters such that each character in such string occurs **an odd number of times**.
     * The returned string must contain only lowercase English letters. If there are multiples valid strings, return **any** of them.
     * 
     * @param n the number of characters in the string
     * @return a string with `n` characters such that each character in such string occurs **an odd number of times**
     */
    public String generateTheString(int n) {
        StringBuilder result = new StringBuilder();
        // Generate 'a' characters to make the count of 'a' odd
        for (int i = 0; i < n - 1; i++) {
            result.append('a');
        }
        // Add any odd character to make the length of the string 'n'
        result.append('b');
        return result.toString();
    }
}