package com.solution;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * This class is used to solve the problem of finding the maximum number of times a word is repeating in a sequence.
 * 
 * @author wanio
 */
public class Solution {
    public int maxRepeating(String sequence, String word) {
        int max = 0;
        String regex = "(?=" + word + "){1,}";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(sequence);
        while (matcher.find()) {
            int k = 0;
            String temp = matcher.group();
            while (temp.equals(word)) {
                k++;
                temp = matcher.find() ? matcher.group() : "";
            }
            max = Math.max(max, k);
        }
        return max;
    }
}