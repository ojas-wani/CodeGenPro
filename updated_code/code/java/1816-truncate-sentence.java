package com.abbreviation;

import java.util.Arrays;

public class Solution {
    /**
     * Truncates a sentence such that it contains only the first k words.
     *
     * @param s the sentence
     * @param k the number of words to keep
     * @return the truncated sentence
     */
    public String truncateSentence(String s, int k) {
        String[] words = s.split(" "); // split the sentence into words
        StringBuilder result = new StringBuilder(); // create a StringBuilder to build the result

        for (int i = 0; i < k; i++) { // loop through the first k words
            result.append(words[i]).append(" "); // append each word to the result
        }

        return result.toString().trim(); // return the result, trimmed to remove trailing space
    }
}