package com.example;

import java.util.ArrayList;
import java.util.List;

/**
 * This is a class for mapping string to English lowercase characters based on the given mapping rules.
 */
public class Solution {
    public String freqAlphabets(String s) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            if (i + 3 <= s.length() && s.substring(i, i + 3).equals("###")) {
                sb.append((char) (Integer.parseInt(s.substring(i + 1, i + 3)) - 0 + 'a'));
                i += 3;
            } else if (i + 2 <= s.length() && s.substring(i, i + 2).equals("#")) {
                sb.append((char) (s.charAt(i + 1) - '0' + 'a'));
                i += 2;
            } else {
                sb.append((char) (s.charAt(i) - '0' + 'a'));
                i++;
            }
        }
        return sb.toString();
    }
}