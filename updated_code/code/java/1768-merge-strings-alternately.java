package com.solution;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Solution {
    /**
     * Merge two strings by adding letters in alternating order, starting with word1. If a string is longer than the other, 
     * append the additional letters onto the end of the merged string.
     * 
     * @param word1 the first string
     * @param word2 the second string
     * @return the merged string
     */
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int minLength = Math.min(word1.length(), word2.length());
        for (int i = 0; i < minLength; i++) {
            merged.append(word1.charAt(i));
            merged.append(word2.charAt(i));
        }
        merged.append(word1.substring(minLength));
        merged.append(word2.substring(minLength));
        return merged.toString();
    }
}