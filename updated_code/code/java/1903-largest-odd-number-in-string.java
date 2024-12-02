package com.example.solution;

import java.util.StringJoiner;

public class Solution {
    public String largestOddNumber(String num) {
        StringJoiner result = new StringJoiner("");
        for (int i = num.length() - 1; i >= 0; i--) {
            if ((num.charAt(i) - '0') % 2 != 0) {
                for (int j = i; j >= 0; j--) {
                    if (isOddInteger(num.substring(j, i + 1))) {
                        result.add(num.substring(j, i + 1));
                    }
                }
            }
        }
        return result.isEmpty() ? "" : result.toString();
    }

    private boolean isOddInteger(String s) {
        int val = Integer.parseInt(s);
        return val % 2 != 0;
    }
}