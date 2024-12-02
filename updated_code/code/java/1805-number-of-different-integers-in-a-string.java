package com.example.solution;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int numDifferentIntegers(String word) {
        String[] nums = word.split("[^0-9]+");
        Set<String> set = new HashSet<>();
        for (String num : nums) {
            if (!num.isEmpty()) {
                set.add(leadingZeroTrim(num));
            }
        }
        return set.size();
    }

    private String leadingZeroTrim(String num) {
        String result = num;
        while (result.startsWith("0") && result.length() > 1) {
            result = result.substring(1);
        }
        return result;
    }
}