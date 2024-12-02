package com.example;

/**
 * This class checks if one string swap can make the two input strings equal.
 */
public class Solution {
    /**
     * This method checks if one string swap can make the two input strings equal.
     *
     * @param s1 the first input string
     * @param s2 the second input string
     * @return true if one string swap can make the two strings equal, false otherwise
     */
    public boolean areAlmostEqual(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false;
        }

        int diff1 = -1, diff2 = -1;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (diff1 != -1) {
                    return false;
                }
                diff1 = i;
            }
        }

        if (diff1 == -1) {
            return true;
        }

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == s2.charAt(diff1) && diff1 != i) {
                diff2 = i;
                break;
            }
        }

        return diff2 != -1 && s1.charAt(diff1) == s2.charAt(diff2);
    }
}