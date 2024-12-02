package com. improvedCode;

import java.util.*;

public class Solution {
    /**
     * Given an alphanumeric string `s`, return _the **second largest** numerical
     * digit that appears in _`s` _, or_`-1` _if it does not exist_.
     * 
     * @param s the input string
     * @return the second largest numerical digit, or -1 if it does not exist
     */
    public int secondHighest(String s) {
        Set<Integer> set = new HashSet<>();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                set.add(Integer.parseInt(String.valueOf(c)));
            }
        }
        if (set.size() < 2) {
            return -1;
        }
        int secondHighest = -1;
        for (int num : set) {
            if (num > secondHighest && num != Collections.max(set)) {
                secondHighest = num;
            }
        }
        return secondHighest;
    }
}