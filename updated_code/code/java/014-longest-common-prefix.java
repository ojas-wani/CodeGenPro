package com.example;

import java.util.Arrays;

/**
 * This class is responsible for finding the longest common prefix string amongst an array of strings.
 */
public class Solution {

    /**
     * This method finds the longest common prefix string amongst an array of strings.
     * If there is no common prefix, it returns an empty string.
     * @param strs  The array of strings.
     * @return  The longest common prefix string.
     */
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        Arrays.sort(strs);
        
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }
        
        return prefix;
    }
}