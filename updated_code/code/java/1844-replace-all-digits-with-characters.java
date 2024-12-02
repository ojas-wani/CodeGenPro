package com.problem;

/**
 * This class will replace all digits with characters based on a certain shift function.
 */
public class Solution {

    /**
     * This method will replace all digits in a given string with characters based on a certain shift function.
     * 
     * @param s The input string that needs to be processed.
     * @return The string with all digits replaced.
     */
    public String replaceDigits(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c;
            if (i % 2 != 0) {
                // Calculate the shift value
                int shift = Integer.parseInt(String.valueOf(s.charAt(i)));
                // Calculate the new character
                c = (char) ((s.charAt(i - 1) - 'a' + shift) % 26 + 'a');
            } else {
                c = s.charAt(i);
            }
            result.append(c);
        }
        return result.toString();
    }
}