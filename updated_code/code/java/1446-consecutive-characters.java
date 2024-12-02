/**
 * Package: com.wwcs
 * Description: This class contains a method that calculates the power of a string.
 */
package com.wwcs;

import java.util.*;

public class Solution {
    /**
     * Calculate the power of a string.
     * 
     * @param s the input string
     * @return the power of the string
     */
    public int maxPower(String s) {
        int maxPower = 0;
        char currentChar = s.charAt(0);
        int currentCount = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == currentChar) {
                currentCount++;
            } else {
                maxPower = Math.max(maxPower, currentCount);
                currentChar = s.charAt(i);
                currentCount = 1;
            }
        }

        return Math.max(maxPower, currentCount);
    }
}