package com.leetcode;

import java.util.*;

public class Solution {
    public String reformat(String s) {
        // Count the number of letters and digits in the string
        int letterCount = 0;
        int digitCount = 0;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                letterCount++;
            } else {
                digitCount++;
            }
        }

        // Check if it is possible to reformat the string
        if (Math.abs(letterCount - digitCount) > 1) {
            return "";
        }

        // Create a list to store letters and digits
        List<Character> letters = new ArrayList<>();
        List<Character> digits = new ArrayList<>();

        // Separate letters and digits
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.add(c);
            } else {
                digits.add(c);
            }
        }

        // Build the result string
        StringBuilder result = new StringBuilder();
        while (!letters.isEmpty() || !digits.isEmpty()) {
            if (!digits.isEmpty()) {
                result.append(digits.get(0));
                digits.remove(0);
            }
            if (!letters.isEmpty()) {
                result.append(letters.get(0));
                letters.remove(0);
            }
        }

        return result.toString();
    }
}