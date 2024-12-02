package com.example;

import java.util.HashSet;
import java.util.Set;

/**
 * This class is used to count the number of good substrings of length 3 in a given string.
 */
public class Solution {

    /**
     * This method is used to count the number of good substrings of length 3 in a given string.
     * 
     * @param s The input string.
     * @return The number of good substrings of length 3.
     */
    public int countGoodSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length() - 2; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = i; j < i + 3; j++) {
                set.add(s.charAt(j));
                if (set.size() == 3) {
                    count++;
                }
            }
        }
        return count;
    }
}