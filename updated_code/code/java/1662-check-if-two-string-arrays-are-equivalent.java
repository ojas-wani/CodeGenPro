package com.ww.study;

/**
 * Check if two string arrays are equivalent
 */
public class Solution {
    /**
     * Check if two string arrays are equivalent
     * 
     * @param word1 the first string array
     * @param word2 the second string array
     * @return true if the arrays represent the same string, false otherwise
     */
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        final String[] word1Copy = word1;
        final String[] word2Copy = word2;

        for (String str : word1Copy) {
            sb1.append(str);
        }
        for (String str : word2Copy) {
            sb2.append(str);
        }

        return sb1.toString().equals(sb2.toString());
    }
}